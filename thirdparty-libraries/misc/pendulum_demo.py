# %%
from datetime import datetime

import pendulum

pendulum.now()

# %%
pendulum.now("Europe/Paris")

# %%
pendulum.now().in_timezone("Europe/Paris")
# %%
pendulum.datetime(2021, 12, 6)

# %%
# today, yesterday, tomorrow

pendulum.yesterday()

# %%
pendulum.tomorrow()

# %%
# 从给定格式生成日期：https://pendulum.eustace.io/docs/#formatter
pendulum.from_format("2020-01-01 01:02:03", "YYYY-MM-DD HH:mm:ss", tz="local")

# %%
pendulum.from_timestamp(60)

# %%
# 从python datetime生成日期
pendulum.instance(datetime.now(), tz="local")


# %%
pendulum.parse("1992-02-23T02:01:59")


# %%
# set global locale
pendulum.set_locale("zh")
pendulum.now().format("YYYY-MM-DD 第Qo季度 今年第DDD天 dddd HH:mm:ss z")


# %%
pendulum.now(tz="local").set(year=1992, month=10, day=18).on(1990, 1, 10).at(
    12, 0, 0
).to_datetime_string()


# %%
pendulum.now().add(years=10).subtract(months=20).add(seconds=60)


# %%
pendulum.now().previous(pendulum.WEDNESDAY)


# %%
pendulum.now().next(pendulum.SUNDAY)

# %%
# 流畅式日期
pendulum.now().set(1992, 12, 1).on(1990, 1, 1).at(10, 30, 0).to_datetime_string()

# %%
pendulum.now().is_leap_year()


# %%
pendulum.now().is_birthday(pendulum.now().add(years=10))


# %%
dt1 = pendulum.datetime(2021, 12, 6, 10, 0, 0)
dt2 = pendulum.datetime(2021, 12, 6, 18, 0, 0)
dt1.diff(dt2).in_hours()


# %%
# 单位可以是年月日时分秒年代世纪
pendulum.now().start_of("century")


# %%
pendulum.now().end_of("century")


# %%
pendulum.now().in_tz("UTC")


# %%
duration = pendulum.duration(years=1, days=1, minutes=40)
duration.years


# %%
duration.total_days()


# %%
duration.in_days()


# %%
duration.in_words()

# %%
