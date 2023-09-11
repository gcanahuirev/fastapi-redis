# Simple queuing system with redis

## Requirements
- Python >= 3.11
- PDM package manager
- Redis instance up and running
- Curl or any http client

## Installation
1. Add the `.env` file and install dependencies
```shell
> pdm install
```
2. Exec virtual env for python
```
> source .venv/bin/activate
```
3. See the scripts available at `pyproject.toml` file
4. Check redis instance up and use a redis cli or [gui](https://github.com/qishibo/AnotherRedisDesktopManager)

## Use cases
### Queue system with fastapi
- Run the producer script, then view data in redis
```sh
> pdm run start_msg_pub
```
- Finally run the consumer script
```sh
> pdm run start_msg_sub
```

### Queue system without fastapi
- Run the fastapi server,
```sh
> pdm run dev
```
then run the request, where 5 and 8 are the input values
```sh
> curl -X POST localhost:8000/job -H "Content-Type: application/json" -d '{"lowest": 5, "highest": 8}'
```
- Finally run the consumer script
```sh
> pdm run start_num_sub
```

*NOTE*:

You can change the amount of test data in `src/producer/msg.py`, where `30` is amount and `1` the delay in seconds
```python
if __name__ == "__main__":
    main(10, 1)
```