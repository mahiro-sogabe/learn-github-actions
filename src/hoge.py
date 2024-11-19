import time


def get_timestamp() -> int:
    """現在日時をエポックミリ秒で取得

    Returns
    -------
    int
        エポックミリ秒
    """
    return int(time.time() * 1000)


def convert_timestamp_to_datetime(timestamp: int) -> str:
    """エポックミリ秒を日時文字列に変換

    Parameters
    ----------
    timestamp : int
        エポックミリ秒

    Returns
    -------
    str
        日時文字列 (yyyy/MM/dd hh:mm:ss)
    """
    dt = time.localtime(timestamp / 1000)
    return time.strftime("%Y/%m/%d %H:%M:%S", dt)


if __name__ == "__main__":
    timestamp = get_timestamp()
    datetime_str = convert_timestamp_to_datetime(timestamp)
    print("--------------------")
    print(f"{'エポックミリ秒:':<15}{timestamp}")
    print(f"{'日時文字列:':<15}{datetime_str}")
