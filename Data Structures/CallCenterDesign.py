class Call(object):
  def __init__(self, customer_id, purpose):
    self.customer_id = customer_id
    self.purpose = purpose
  
  def terminate(self):
    return "Please come to Site-office."
    
class Employee(object):
  def __init__(self):
    self.employee_id = None
    self.employee_name = None
  
  def process_call(self, call):
    try:
      self.solve_problem(call)
    catch:
      return None
      
  def solve_problem(self, call):
    pass

class CallDispatcher(object):
  def __init__(self):
    self.respondent_queue = 10
    self.manager_queue = 5
    self.director = 1
    
  def start_call_listen(self):
    # Start server
    if call:
      if self.respondent_queue > 0:
        employee = Repondent()
        self.respondent_queue -= 1
        if not dispatchCall(employee, call):
          if self.manager_queue > 0:
            manager = Manager()
            self.manager_queue -= 1
            if not dispatchCall(manager, call):
              director = Director()
              if not self.dispatchCall(director, call):
                call.terminate()

  def dispatchCall(employee, call):
    if employee.process_call(call):
      return True
    else:
      return False

class Repondent(Employee):
  def __init__(self):
    super(Repondent, self).__init__()
  
  def solve_problem(self, call):
    pass
  
class Manager(Employee):
  def __init__(self):
    super(Repondent, self).__init__()
  
  def solve_problem(self, call):
    pass
  
class Director(Employee):
  def __init__(self):
    super(Repondent, self).__init__()
  
  def solve_problem(self, call):
    pass
  
  
CallCenter = CallDispatcher()
CallCenter.start_call_listen()
  
