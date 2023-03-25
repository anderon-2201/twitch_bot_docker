from twitchio.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()

class Bot( commands.Bot ):
    def __init__( self ):
        super().__init__(
            token = os.getenv( 'TOKEN' ),
            prefix = os.getenv( 'PREFIX' ),
            initial_channels = [ os.getenv( 'CHANNELS' ) ]
        )

    async def event_ready( self ):
        print( '\nTwitch_bot has successfully started' )
        print( f'Logged in as | { self.nick }\n' )
        print( f'User id is | { self.user_id }\n' )

    @commands.command()
    @commands.cooldown( 1, 5, commands.Bucket.member )
    async def ping( self, ctx: commands.Context ):
        print( f'{ ctx.author.name } has use !ping' )
        await ctx.send( open( 'assets/messages/ping', 'r' ).read() )

    @commands.command()
    @commands.cooldown( 2, 15, commands.Bucket.user )
    async def help( self, ctx: commands.Context ):
        print( f'{ ctx.author.name } has use !ayuda' )
        await ctx.send( open( 'assets/messages/help', 'r' ).read() )

    @commands.command()
    @commands.cooldown( 2, 15, commands.Bucket.user )
    async def command( self, ctx: commands.Context ):
        print( f'{ ctx.author.name } has use !comandos' )
        await ctx.send( open( 'assets/messages/commands', 'r' ).read() )

    @commands.command()
    @commands.cooldown( 1, 5, commands.Bucket.member )
    async def hello( self, ctx: commands.Context ):
        print( f'{ ctx.author.name } has use !hola' )
        await ctx.send( open( 'assets/messages/hello', 'r' ).read() )

bot = Bot()
bot.run()
