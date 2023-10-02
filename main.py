 import re

print("Welcome To Exerise 11\n"
      "Email Collector\n")
str = """

Email:enquiry@alliance.edu.in   Helpline: +91 80 3093 8100 / 8200 / 4619 9100
Media  Library  News  Webmail  Careers
Alliance University
Conferences
Admissions Open
Select Language
UPDATES:
ABOUT US 
WHY AU 
COLLEGES 
FACULTY
INTERNATIONAL PROGRAMS
PROGRAMS
RESEARCH
ADMISSIONS 
PLACEMENTS
CONTACT US
Contact UsHome Contact Us
 Contact Us Back
 Vice-Chancellor
Dr. Pavana Dibbur
 : vc@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Pro Vice-Chancellor (Academics, Research & Strategy)
Dr. Anubha Singh
 : anubha@alliance.edu.in
 : +91 80 3093 8102

 Registrar
Mr. Madhu Sudan Mishra
 : registrar@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Registrar (Examination & Evaluation)
Dr. Sajan Mathew
 : registrar.exams@alliance.edu.in
 : +91 80 3093 8141

 Director (Placements)
Mr. Mathew Thankachan
 : placement@alliance.edu.in | mathew.t@alliance.edu.in
 : +91 80 3093 8124 | 98444 72674

 Director (International Affairs)
Mr. Rajen Chatterjee
 : rajen.chatterjee@alliance.edu.in
 : +91 80 3093 8075

 Director (Admissions)
Mr. Abhay Chebbi
 : abhay.chebbi@alliance.edu.in
 : +91 96636 46464

 Human Resources Department
 : hrd@alliance.edu.in
 : +91 80 3093 8210 / 8204

 Student Verification 
Office of Registrar (Examination & Evaluation)
 : edu.verify@alliance.edu.in
 : +91 80 3093 8100 / 8200 | +91 80 4619 9100

Beijing Institute of Technology
China
Nanjing University of Aeronautics and Astronautics
Nanjing University of Aeronautics and Astronautics
China
The Sino-British College, USST,
The Sino-British College, USST,
China
INSEEC
INSEEC
France
IPAC School of Management
IPAC School of Management
France
ISEP
ISEP
France
Paris School of Business
Paris School of Business
France
Telecom School of Management
Telecom School of Management
France
Telecom SudParis
Telecom SudParis
France
Toulouse Business School
Toulouse Business School
France
Berlin School of Economics and Law
Berlin School of Economics and Law
Germany
European Business School
European Business School

USA
Georgia State University
Georgia State University
USA
Kennesaw State University
Kennesaw State University
US
Oakland University
Oakland University
USA
San Jose State University
San Jose State University
USA
The University of Memphis
The University of Memphis
USA
Webber International University
Webber International University
USA
 International Programs
 Testimonials
 My two years at Alliance University have groomed me to be a confident individual ready to enter the corporate world and has deepened this confidence by helping me get a job in my dream organization. Alliance with its state of the art facilities, competitive curriculum, varied cultural mix and strong faculty base has motivated and guided m...  Read More

 Kiran Varghese Jacob Kiran Varghese Jacob
Google Google
 Top University in India for MBA LAW Engineering & Arts and the Humanities
Alliance University is a private University established in Karnataka State by Act No.34 of year 2010 and is recognized by the University Grants Commission (UGC), New Delhi... 

"""

email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",str)
print(f"The emails we found are :\n{email}")
