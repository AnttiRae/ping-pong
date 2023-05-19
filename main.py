import os

from fastapi import FastAPI


class Counter:
    number_of_pings = 0

    def __init__(self, pong_file='pong.log'):
        self.pong_file = pong_file

    def get_number_of_pings(self):
        return self.number_of_pings

    def increment_pings_by_one(self):
        self.number_of_pings += 1

    def write_number_of_pongs_to_file(self):
        with open(self.pong_file, 'w+') as file:
            file.write(f'Ping / Pongs: {self.number_of_pings}')


app = FastAPI()
pong_log_file = os.environ.get('PONG_FILE')
counter = Counter(pong_file=pong_log_file)


@app.get("/")
async def root():
    return "pong app"


@app.get("/pingpong")
async def pong():
    counter.increment_pings_by_one()
    counter.write_number_of_pongs_to_file()
    return {
        "pongs": counter.get_number_of_pings()
    }
