import streamlit as st
from library_module import Library
from user_module import UserSystem

st.title("📚 Library Management System")

# User login / registration
option = st.sidebar.selectbox("Choose Action:", 
                              ["Register User", "Login User", "Exit"])

if option == "Register User":
    st.header("Register New User")
    name = st.text_input("Enter Name")
    uid = st.text_input("Enter User ID (4–10 digits)")

    if st.button("Register"):
        if UserSystem.validate_name(name) and UserSystem.validate_id(uid):
            UserSystem.save_user_record(name, uid)
            st.success("User Registered Successfully!")
        else:
            st.error("Invalid Name or User ID")

elif option == "Login User":
    st.header("Login")
    uid = st.text_input("Enter User ID")

    if st.button("Login"):
        if UserSystem.verify_user(uid):
            st.success("Login Successful!")
            lib = Library()

            st.subheader("Book Operations")
            choice = st.radio("Choose: ", ["Show Books", "Borrow Book", "Return Book"])

            if choice == "Show Books":
                st.write("### Available Books")
                data = []
                for b in lib.books.values():
                    data.append([b.book_id, b.title, b.author, b.copies])
                st.table(data)

            elif choice == "Borrow Book":
                book_id = st.text_input("Enter Book ID to Borrow:")
                if st.button("Borrow"):
                    if book_id in lib.books and lib.books[book_id].copies > 0:
                        lib.books[book_id].copies -= 1
                        lib.save_books()
                        lib.save_transaction(uid, book_id, "BORROW")
                        st.success("Book Borrowed Successfully!")
                    else:
                        st.error("Invalid ID or No Copies Available")

            elif choice == "Return Book":
                book_id = st.text_input("Enter Book ID to Return:")
                if st.button("Return"):
                    if book_id in lib.books:
                        lib.books[book_id].copies += 1
                        lib.save_books()
                        lib.save_transaction(uid, book_id, "RETURN")
                        st.success("Book Returned Successfully!")
                    else:
                        st.error("Invalid Book ID")
        else:
            st.error("User does not exist!")

else:
    st.write("Thank you!")

