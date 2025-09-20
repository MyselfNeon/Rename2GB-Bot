from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(
        text="""
        <body style="
            background-color:black; 
            display:flex; 
            justify-content:center; 
            align-items:flex-start; 
            height:100vh; 
            margin:0; 
            font-family:sans-serif; 
            padding-top:20vh; 
            font-size:4rem; 
            color:#39FF14; 
            text-shadow: 0 0 5px #39FF14, 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 40px #39FF14;
            animation: glow 1.5s infinite alternate;
        ">
            || NeonFiles ||
        </body>
        <style>
            @keyframes glow {
                from { text-shadow: 0 0 5px #39FF14, 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 40px #39FF14; }
                to { text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14, 0 0 60px #39FF14; }
            }
        </style>
        """,
        content_type="text/html"
    )


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
