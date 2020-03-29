def say_hello(name):
    print(f'Hello {name}')
# just a simple functions
# we assign a variable to that function and consider it as a data itself
say_hello_2 = say_hello
say_hello_2('Johnny')

# this flag changes the behaviour of the fetch_data function later on
ENVIRONMENT = 'prod'

def fetch_data_real():
    print('Doing some very time intensive operations...')
# this could be the real function where it takes lot of time to run the code
# or we don't want to apply directly in the production stage
def fetch_data_fake():
    print('Returning fake data')
    return {
        'name': 'Jane Doe',
        'age': 34
    }

fetch_data = fetch_data_real if ENVIRONMENT == 'prod' else fetch_data_fake
# the whole fetch_data process is now literally our data
data = fetch_data()