from pydantic 
import BaseClass

# It's possible to have multiple classes with many of the same fields, except one is specialized for user input, one for output, and one for internal use. 
# Some reasons for these variants could include the following: 
#  * Remove some sensitive information from the output 
#  * Add fields to the user input (like a creation date and time).

class TagIn(BaseClass):
    tag: str

class Tag(BaseClass):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseClass):
    tag: str
    created: datetime

