# Home Server as a NAS

This directory contains instructions for setting up a home server as a NAS (Network-Attached Storage).

**Note:**  
- Work in progress.  
- The goal is to create a web app for file uploads and downloads.  
- No encryption or redundancy implemented yet.

---

## **Current Plan**

### User Login:
- Upon login, if a new user is detected:
  - Create a new directory for the user.
  - Generate a "Sym_KEY" in MongoDB Atlas for symmetric key encryption/decryption (TODO LATER).
  
- Define a **MAX number of users** and **storage limit per user** (Managed via MongoDB or SQL).

---

### Dashboard (Post-login):
After logging in, users are presented with a dashboard containing 3 options:

1. **View Files**  
   - Display file names and file types.

2. **Upload**  
   - Plan: Break files into 10MB chunks and upload in parallel (Max parallel processes = 10).
   - Files will be encrypted using the "Sym_KEY" before being stored in the user’s directory.
   - Naming format for files: `"FILE_NAME__TYPE__part_of_chunk__Total_chunks"` (no extension).

3. **Download**  
   - Display files that the user has uploaded, along with their **storage used** and **storage left**.
   - Select a file to download (TODO LATER).

---

### File Database:
- For each user, maintain a single database table containing:
  1. Name of file.
  2. Type of file.
  3. Size of file.
  4. Date of upload.
  5. `USER_ID` from the login system.

*Note:* Storing data in one table for all users is preferred to avoid excessive table creation.

---

### Any help or suggestions would be appreciated! Feel free to reach out if you have ideas or feedback. 
