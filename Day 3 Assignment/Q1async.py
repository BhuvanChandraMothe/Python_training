import aiohttp
import asyncio
import time
import sys 

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    

#download a link 

async def download(url):
    async with aiohttp.ClientSession() as sess :
        async with sess.get(url) as resp:
            return await resp.text()
            
async def main():
    url = "http://httpbin.org/get"
    res = await download(url)
    return res

async def mainp(n):
     urls = ["http://httpbin.org/get" for _ in range(n)]
     res = await asyncio.gather(*[download(u) for u in urls])
     return res
    
if __name__ == '__main__':
    st = time.time()
    asyncio.run(main())
    print("Time taken", time.time()-st, "secs")
    print('now running in parallel')
    asyncio.run(mainp(10))
    print("Time taken", time.time()-st, "secs")