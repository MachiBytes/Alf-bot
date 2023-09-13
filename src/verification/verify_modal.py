import discord
from discord.ui import Modal, TextInput, View, Button
from src import settings
from src.verification import reject_modal


class VerifyModal(Modal, title="Fill in the details to get verified"):
    full_name = TextInput(
        style=discord.TextStyle.short,
        label="Full Name",
        required=True,
        placeholder="LastName, FirstName MiddleInitial"
    )

    email = TextInput(
        style=discord.TextStyle.short,
        label="Personal Gmail",
        required=True,
        placeholder="abc@gmail.com",
    )
    
    clubId = TextInput(
        style=discord.TextStyle.short,
        label="Club ID",
        required=True,
        placeholder="AWS-CC-2023-####",
    )

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction) -> None:
        user = interaction.user

        # Create an embed of their response
        embed = discord.Embed(title="Verification Request", description=f"{user.name} requested for their account to be verified.")
        embed.add_field(name="Full Name", value=self.full_name.value, inline=False)
        embed.add_field(name="Personal Gmail", value=self.email.value, inline=False)
        embed.add_field(name="Club ID", value=self.clubId.value, inline=False)
        embed.add_field(name="Instructions", value="Choose from the buttons below to accept or reject this user.")
        embed.set_thumbnail(url=str(user.display_avatar))

        # Send a ticket to the ticket channel
        ticket_channel = self.bot.get_channel(settings.VERIFY_TICKET_CHANNEL)

        # Callbacks
        async def accept(interaction):
            # Add user's discord ID to the database (not yet implemented)
            guild = interaction.guild
            verified_role = guild.get_role(settings.VERIFIED_ROLE_ID)
            await user.add_roles(verified_role)

            embed = discord.Embed(title="Verification request", description="Congratulations! Your verification request has been accepted. We officially welcome you onboard the AWSCC Discord Server!")
            await user.send(embed=embed)
            await ticket_message.delete()

        async def reject(interaction):
            reject = reject_modal.RejectModal(user)
            await interaction.response.send_modal(reject)

        accept_button = Button(label="Accept", style=discord.ButtonStyle.green)
        accept_button.callback = accept
        reject_button = Button(label="Reject", style=discord.ButtonStyle.red)
        reject_button.callback = reject

        view = View(timeout=None)
        view.add_item(accept_button)
        view.add_item(reject_button)

        ticket_message = await ticket_channel.send(embed=embed, view=view)

        # End the interaction
        await interaction.response.send_message(content="Verification is being processed...", ephemeral=True, delete_after=3)

    async def on_error(self, interaction, error: Exception) -> None:
        return await super().on_error(interaction, error)