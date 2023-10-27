import discord
from src.database import tickets_json
from src.verification import verify_modal, reject_modal
from src import settings

class VerifyView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="Get verified!", style=discord.ButtonStyle.primary, emoji="\u2705", custom_id="verify_view:get_verified")
    async def get_verified(self, interaction, button):
        # Create the VerifyModal
        verify = verify_modal.VerifyModal(self.bot)
        await interaction.response.send_modal(verify)

class TicketView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green, custom_id="ticket:accept")
    async def accept_ticket(self, interaction, button):
        # Add user's discord ID to the database (not yet implemented)
        guild = interaction.guild
        verified_role = guild.get_role(settings.VERIFIED_ROLE_ID)
        
        # Get user from message_id
        user_id = tickets_json.get_user_from_message(interaction.message.id)
        user = interaction.guild.get_member(user_id)

        await user.add_roles(verified_role)

        embed = discord.Embed(title="Verification request", description="Congratulations! Your verification request has been accepted. We officially welcome you onboard the AWSCC Discord Server!")
        await user.send(embed=embed)
        tickets_json.remove_ticket(interaction.message.id)
        await interaction.message.delete()

    @discord.ui.button(label="Reject", style=discord.ButtonStyle.red, custom_id="ticket:reject")
    async def reject_ticket(self, interaction, button):
        # Get user from message_id
        user_id = tickets_json.get_user_from_message(interaction.message.id)
        user = interaction.guild.get_member(user_id)

        reject = reject_modal.RejectModal(user)
        await interaction.response.send_modal(reject)
    