# Smart Mars Frontend

## Overview
Smart Mars Frontend is a React-based web application designed for the Bob the Builder project. It serves as the user interface, providing navigation and foundational pages for employees, materials, and projects.

## Features
- **React + React Router** for smooth navigation
- **Static Hosting** via AWS S3 and CloudFront
- **Predefined Pages**: Home, Login, Employees, Materials, Projects
- **Styled UI** with responsive design

## Project Structure
```
smart-mars-frontend/
├── public/
│   ├── bob-waving.png  # Static image for homepage
│   ├── index.html      # Main HTML shell
├── src/
│   ├── components/     # Reusable UI components
│   ├── routes/         # Page components
│   ├── App.js          # Main app with routing
│   ├── index.js        # React entry point
├── .gitignore
├── package.json        # Dependencies and scripts
├── README.md           # Project documentation
```

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone git@github.com:Team-Tethys/smart-mars-frontend.git
cd smart-mars-frontend
```
### **2. Install Dependencies**
```sh
npm install
```
### **3. Run Locally**
```sh
npm start
```
### **4. Build for Production**
```sh
npm run build
```

## Deployment
### **1. Upload to S3**
```sh
aws s3 sync build/ s3://bob-the-builder-frontend
```
### **2. Invalidate CloudFront Cache**
```sh
aws cloudfront create-invalidation --distribution-id <DISTRIBUTION_ID> --paths "/*"
```

## Future Enhancements
- Integrate backend API
- Implement authentication
- Enhance UI with Tailwind or Material UI

## License
This project is maintained by Team Tethys. All rights reserved.

