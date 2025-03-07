"""
+------------------+
|    Student      | (Abstract Class)
|------------------|
| - name: str     |
| - id: str       |
| - grades: Dict  |
| - is_active: bool |
|------------------|
| + clone()       | (Abstract Method)
+------------------+
        ▲
        │
+----------------------+
|  ConcreteStudent    | (Concrete Class)
|----------------------|
| + add_grade()       |
| + get_average_grade()|
| + toggle_active_status()|
| + clone()           | (Deep Copy Implementation)
+----------------------+

     Cloning Process
---------------------------
   student1 (Original)
      |
      |  clone()
      ▼
   student2 (Deep Copy)


"""