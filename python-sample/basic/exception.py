# %%
class MyError(Exception):
    pass


# %%
try:
    raise MyError()
except (NameError, ValueError) as ex:
    print(f"This is a NameError:{ex}")
except MyError as ex:
    print("This is MyError")
    ex.add_note("adding extra exception info")
    raise
else:
    print("executed when no exception raised")
finally:
    print("This is finally clause, always executed")
