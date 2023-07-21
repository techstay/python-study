# %%
import asyncio
import socket

socket.gethostbyname("www.baidu.com")

# %%

socket.gethostname()
# %%

# TODO: 程序逻辑有些问题，没办法正常运行
host = socket.gethostbyname("localhost")
port = 20086


async def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"connection established: {addr}")
        for i in range(5):
            conn.send(f"hello {i}\n".encode())
            await asyncio.sleep(0.5)
        print("send finished")


async def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        await asyncio.sleep(1)
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode())


async def socket_demo():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(server())
        tg.create_task(client())


if __name__ == "__main__":
    asyncio.run(socket_demo())
# %%
