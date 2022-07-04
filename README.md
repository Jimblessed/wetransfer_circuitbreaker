# wetransfer_circuitbreaker

The Circuit Breaker Pattern is a way to build resilient and fault tolerant systems.
It is software implementation of an electrical circuit breaker which is a device designed to protect an electrical circuit from damage by interupting
current flow to protect an equipment from damage.

The basic idea behind the circuit breaker is very simple. 
You wrap a protected function call in a circuit breaker object, which monitors for failures. 
Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error, 
without the protected call being made at all. Source https://martinfowler.com/bliki/CircuitBreaker.html

The Circuit Breaker has 3 states: 

"CLOSED": When all services are working and the remote calls are returning without any errors.

"OPEN": The Open state rejects all requests for a certain amount of time and returns an error.

"HALF-OPEN": After a specified timeout, the breaker transitions from open to half-open to test the remote service.
If the call is successful, it then transitions to closed or open again if the call fails.

Installation
===========

Make sure Python 3.xxx is installed on your PC and clone this repo.


Instruction to test:
====================

1. In windows, Open PowerShell with Admin privileges.
2. Install requests, flask and ipython by running:

pip install requests
pip install Flask
pip install ipython

3. Navigate to the folder containing our .py files (circuitBreaker)
4. run $env:FLASK_APP="main.py"
5. run flask run 
> 

These are to run our mock flask server

6. Open another PowerShell window, and navigate to our folder containing our .py files((circuitBreaker))
7. run: python


Now let's import our created libraries(note where our are getting the import from must have the same name as the .py):

8. from Circuit_Breaker import CircuitBreaker  
9. from testCode import make_request, faulty_endpoint, success_endpoint
10. breaker = CircuitBreaker(make_request, exceptions=(Exception,), error_threshold=3, time_window=20)
11. breaker.make_remote_call(success_endpoint)

See my success output result from the file "test_results.txt". you should get the same thing

And when we also try the faulty mock server:

12. breaker.make_remote_call(faulty_endpoint)

You should get an exception error, and if you try up to 3 times which is our error_threshold, it should finally OPEN the State and if you try any other, it will tell you to wait until the time_window or delay elapes

After our time_windows elapes, if your try the good server, it will bring the state of the breaker back to CLOSE, which allows flow of requests.

***You can also run the python source files "faulty_endpoint" and "success_endpoint" instead of manually typing the code.

