# Swapify - One swap at a time.

A backend for a Barter System application where users can trade items directly with each other, keeping track of transactions, messaging, and item listings.

## Features

- **Item Listings**: Users can list items they want to barter.
- **Transactions**: Initiate, accept, reject, or complete barter transactions.
- **Messaging**: Users can send messages during transactions.
- **Authentication**: User registration and login using JWT.
- **Security**: Protection against XSS, NoSQL injection, and HTTP parameter pollution.

## Tech Stack

- **Backend**: Node.js, Express.js
- **Database**: MongoDB (MongoDB Atlas)
- **Authentication**: JSON Web Token (JWT)
- **Other Dependencies**:
  - **mongoose** for MongoDB ORM
  - **express-rate-limit** for rate-limiting requests
  - **helmet** for setting security headers
  - **express-mongo-sanitize** for NoSQL injection protection
  - **xss-clean** for XSS protection
  - **bcryptjs** for hashing passwords
  - **dotenv** for environment variables

## API Endpoints

### 1. **Authentication**

- **POST** `/api/v1/users/signup`: User sign up (register).
- **POST** `/api/v1/users/login`: User login (JWT-based).
- **POST** `/api/v1/users/forgotPassword`: Sends email to reset password using nodemailer.
- **POST** `/api/v1/users/resetPassword/:token`: Link sent to user via email.

### 2. **Items**

- **GET** `/api/v1/items`: Get all items.
- **POST** `/api/v1/items`: Create a new item.
- **GET** `/api/v1/items/:id`: Get details of an item by ID.
- **PUT** `/api/v1/items/:id`: Update an item.
- **DELETE** `/api/v1/items/:id`: Delete an item.

### 3. **Transactions**

- **POST** `/api/v1/transactions`: Create a new transaction.
- **GET** `/api/v1/transactions`: Get all transactions.
- **GET** `/api/v1/transactions/:id`: Get details of a specific transaction.
- **PATCH** `/api/v1/transactions/:id/status`: Update transaction status (e.g., Accept, Reject, Complete).
- **POST** `/api/v1/transactions/:id/messages`: Send a message in the transaction.

## Deployment

The application is deployed on [Vercel](https://vercel.com/). You can visit the live API at:

- **Live API URL**: [https://barter-backend-five.vercel.app/](https://barter-backend-five.vercel.app/)
- **API Publication**: [https://documenter.getpostman.com/view/31551887/2sAYQanBmZ](https://documenter.getpostman.com/view/31551887/2sAYQanBmZ)

Created by [Prateek Prasanna Savanur](https://prateeksavanur.xyz).
