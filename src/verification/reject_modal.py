import discord
from discord.ui import Modal, TextInput
from src.database import tickets_json

class RejectModal(Modal, title="Verification request rejected."):
    reason = TextInput(
        style=discord.TextStyle.long,
        label="Reason",
        required=True,
        placeholder="Your verification request is denied because..."
    )

    def __init__(self, user):
        super().__init__()
        self.user = user
    
    async def on_submit(self, interaction):
        rejector = interaction.user
        embed = discord.Embed(title="Verification Request Denied.", description=f"Hi {self.user.name}! Your verification request has been denied by {rejector.name}. If you believe that this is a mistake, please contact Mark Achiles Flores Jr. thru Facebook or aki_9716 thru Discord.")
        embed.add_field(name="Reason", value=self.reason.value, inline=False)

        await self.user.send(embed=embed)

        # End interaction
        await interaction.response.send_message(content="Verification rejected...", ephemeral=True, delete_after=0.1)
        tickets_json.remove_ticket(interaction.message.id)
        await interaction.message.delete()
    
    async def on_error(self, interaction, error) -> None:
        return await super().on_error(interaction, error)