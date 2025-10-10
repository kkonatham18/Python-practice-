import streamlit as st
from datetime import datetime
books = [
    {"name": "Python Basics", "author": "John Doe", "available": True},
    {"name": "Data Science 101", "author": "Jane Smith", "available": True},
    {"name": "Machine Learning", "author": "Alice Brown", "available": True}
]
borrowed_books = {}
def show_books():
    st.subheader("Available Books")
    for book in books:
        status = "Available" if book["available"] else "❌ Issued"
        st.write(f'**{book["name"]}** by *{book["author"]}* - {status}')


def issue_book(student_name, book_name):
    student = borrowed_books.get(student_name, [])
    if len(student) >= 3:
        st.warning( "You cannot issue more than 3 books.")
        return

    for book in books:
        if book["name"] == book_name and book["available"]:
            book["available"] = False
            student.append({
                "book_name": book_name,
                "issue_date": datetime.today().strftime("%Y-%m-%d")
            })
            borrowed_books[student_name] = student
            st.success(f"Book '{book_name}' issued successfully.")
            return
    st.error("Book not available or does not exist.")


def return_book(student_name, book_name, return_date_str):
    student = borrowed_books.get(student_name, [])
    for record in student:
        if record["book_name"] == book_name:
            issue_date = datetime.strptime(record["issue_date"], "%Y-%m-%d")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
            delta = (return_date - issue_date).days
            fine = 0
            if delta > 7:
                fine = (delta - 7) * 10

            # Update availability
            for book in books:
                if book["name"] == book_name:
                    book["available"] = True
                    break

            # Remove book from borrowed list
            student.remove(record)
            if student:
                borrowed_books[student_name] = student
            else:
                borrowed_books.pop(student_name)

            st.success(f"Book '{book_name}' returned successfully.")
            st.info(f"Days Borrowed: {delta} days")
            if fine > 0:
                st.warning(f"Fine: ₹{fine}")
            else:
                st.success("No fine!")
            return

    st.error("You have not borrowed this book.")


def view_borrowed_books(student_name):
    st.subheader(f"Books borrowed by {student_name}")
    student = borrowed_books.get(student_name, [])
    if not student:
        st.info("You have not borrowed any books.")
        return
    today = datetime.today()
    for record in student:
        issue_date = datetime.strptime(record["issue_date"], "%Y-%m-%d")
        days = (today - issue_date).days
        fine = max(0, (days - 7) * 10)
        st.write(f"**{record['book_name']}** | Issued on: {record['issue_date']} | "
                 f"Days: {days} |Fine: {fine if fine > 0 else 0}")


# Main Streamlit app
def library_system():
    st.title("Library Management System")
    st.markdown("---")
    student_name = st.text_input("Enter your name (Student)")

    if not student_name:
        st.warning("Please enter your name to continue.")
        return

    menu = ["Show Books", "Issue Book", "Return Book", "View Borrowed Books"]
    choice = st.selectbox("Select an action", menu)

    if choice == "Show Books":
        show_books()

    elif choice == "Issue Book":
        show_books()
        book_to_issue = st.text_input("Enter the book name to issue:")
        if st.button("Issue Book"):
            issue_book(student_name, book_to_issue)

    elif choice == "Return Book":
        view_borrowed_books(student_name)
        book_to_return = st.text_input("Enter the book name to return:")
        return_date_str = st.date_input("Select return date", datetime.today()).strftime("%Y-%m-%d")
        if st.button("Return Book"):
            return_book(student_name, book_to_return, return_date_str)

    elif choice == "View Borrowed Books":
        view_borrowed_books(student_name)


# Run the app
if __name__ == "__main__":
    library_system()
