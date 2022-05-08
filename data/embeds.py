import discord

embed = discord.Embed(title="Pomoc", description="Pomoc dotycząca bota Pytanie Czy Wyzwanie", color=0x00aaff)
embed.set_author(name="Robert(Mautyna)")
embed.add_field(name="Prefix bota", value="Prefix bota to pcw!", inline=False)
embed.add_field(name="Początek", value="Na początku musisz ustalić liczbę graczy oraz oznaczyć graczy", inline=True)
embed.add_field(name="Rozgrywka",
                value="Podczas rozgrywki zostaje generowana losowa liczba która odpowiada danemu graczowi",
                inline=True)
embed.add_field(name="Zakończenie",
                value="W czasie gdy gracze będą kończyć grę mogą sprawdzić ile wzieli pytań, ile wyzwań oraz ile dostali kar",
                inline=True)
embed.set_footer(
    text="Aby dowiedzieć się więcej, naciśnij odpowiedni przycisk poniżej")



embedadmin=discord.Embed(title="Admin Help", description="Tutaj znajdziesz wszystkie komendy dla administratora", color=0x00ff1e)
embedadmin.add_field(name="Status Stream", value="pcw!statusStream [status]", inline=False)
embedadmin.add_field(name="Status Idle", value="pcw!statusIdle [status]", inline=False)
embedadmin.add_field(name="Status Busy", value="pcw!statusBusy [status]", inline=False)
