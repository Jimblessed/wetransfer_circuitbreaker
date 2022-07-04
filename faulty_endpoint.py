from Circuit_Breaker import CircuitBreaker  
from testCode import make_request, faulty_endpoint, success_endpoint
breaker = CircuitBreaker(make_request, exceptions=(Exception,), error_threshold=3, time_window=20)
breaker.make_remote_call(faulty_endpoint)