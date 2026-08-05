from fastapi import FastAPI,HTTPException
from pydentic import BaseModel

app= FastAPI()

students={
    "S001":{"name": "Anuj","marks":90, "grade":"A+"},
    "S002":{"name": "Anij","marks":40, "grade":"C"},
    "S003":{"name": "sandesh","marks":80, "grade":"A"},
}

class MarksSubmission(BaseModel):
    student_id: str
    marks: int 
    subject: str

@app.get("/student/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code= 404,
            detail= f"Student with ID {student_id} dose not exists"
        )
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):
    if submission.student_id not in students:
        raise HTTPException(
            status_code= 404,
            detail= f"Student with ID {submission.student_id} dose not exists"
        )
        
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code= 400,
            detail={
                "error": "marks must be between 0 to 100" 
            }
        )
    
    if submission.subject.strip()== "":
        raise HTTPException(
            status_code= 400,
            detail="subject name cannot be empty"
        )
    
    try:
        students[submission.student_id]["marks"]= submission.marks
        return{
                "message": "marks submitted successfully",
                "student": students[submission.student_id]["name"],
                "subject": submission.subject,
                "marks": submission.marks
            }
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail=f"Something went wrong on our side: {str(e)}"
        )