# %%
import datetime as dt

today = dt.date.today()
# %%
now = dt.datetime.now()
# %%
that_day = dt.date(1989, 10, 1)
period = today - that_day
# %%
period.days
# %%
period.days // 365
# %%
now.astimezone(dt.timezone.utc)
# %%
