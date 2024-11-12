<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Designation Management</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 3px 20px;
            border-bottom: 2px solid #e0e0e0;
        }
        .header img {
            height: 50px;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
        }
        .user-info {
            text-align: right;
        }
        .user-info a {
            color: #007bff;
            text-decoration: none;
        }
        .navbar {
            background-color: red;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        .container {
            display: flex;
            padding-top: 80px;
            transition: margin-left 0.3s;
        }
        .sidebar {
            width: 200px;
            background-color: #ffffff;
            padding: 10px;
            border-right: 1px solid #ff0000;
            display: none;
            flex-direction: column;
            position: fixed;
            top: 60px;
            left: 0;
            height: calc(100% - 60px);
            overflow-y: auto;
            z-index: 5;
        }
        .sidebar ul {
            list-style-type: none;
            padding: 0;
        }
        .sidebar ul li {
            padding: 10px;
            color: #333333;
        }
        .sidebar ul li a {
            text-decoration: none;
            color: #333333;
            display: block;
        }
        .sidebar ul li a:hover {
            color: #ff0000;
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #888;
            position: relative;
            bottom: 0;
            width: 100%;
            margin-top: auto;
        }
        .main-content {
            flex-grow: 1;
            padding: 20px;
            background-color: #ffffff;
            margin-left: 200px;
            transition: margin-left 0.3s;
        }
        .sidebar-active .sidebar {
            display: flex;
        }
        .sidebar-active .navbar {
            margin-left: 200px;
        }
        .sidebar-active .container {
            margin-left: 200px;
        }
        .dropdown {
            display: none;
            padding-left: 15px;
            list-style-type: none;
            background-color: #f9f9f9;
            border-left: 2px solid #ff0000;
            margin: 0;
        }
        .dropdown li {
            padding: 5px 0;
        }
        .dropdown li a {
            color: #333333;
            font-size: 14px;
        }
        .dropdown li a:hover {
            color: #ff0000;
        }
        .dropdown.show {
            display: block;
        }
        .arrow {
            font-size: 10px;
            margin-left: 5px;
        }

        /* Styles for form, table, search, and pagination */
        .form-section {
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            font-size: 16px;
            font-weight: bold;
        }

        .form-group input[type="text"], .form-group input[type="radio"] {
            padding: 8px;
            margin: 5px 0;
            font-size: 14px;
            width: 200px;
            margin-top: 5px;
        }

        .form-group input[type="radio"] {
            width: auto;
            margin-left: 20px;
        }

        .button-group button {
            padding: 10px 20px;
            background-color: #ff0000;
            color: white;
            border: none;
            cursor: pointer;
            margin-right: 10px;
            font-size: 16px;
        }

        .button-group button:hover {
            background-color: darkred;
        }

        .search-section {
            margin-bottom: 20px;
        }

        .search-section input {
            padding: 10px;
            width: 100%;
            font-size: 16px;
            margin-top: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .designation-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .designation-table th, .designation-table td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }

        .designation-table th {
            background-color: #f4f4f4;
        }

        .pagination {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }

        .pagination button {
            padding: 10px 20px;
            margin: 0 5px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }

        .pagination button:hover {
            background-color: #0056b3;
        }

        .pagination button.disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">
            <img src="https://storage.googleapis.com/a1aa/image/4JEeyOlRe2vfwoMPFJZxYX3hVQBx1YuhHb49DXnfS4z9JbuOB.jpg" alt="Organization Logo" width="50" height="50">
        </div>
        <div class="title">Share & Care Palliative Care</div>
        <div class="user-info">
            <div>Welcome! <a href="#">John Doe</a></div>
            <div>Last Logged in 31/01/2024 11:12 AM</div>
        </div>
    </header>

    <nav class="navbar" onclick="toggleSidebar()">
        <i class="fas fa-bars menu-icon"></i> Designation
    </nav>

    <div class="container">
        <aside class="sidebar">
            <ul>
                <li><a href="#">+ Donor Registration</a></li>
                <li><a href="#">✍️ Donate Blood</a></li>
                <li><a href="#">🔍 Donor Search</a></li>
                <li>
                    <a href="#" id="mastersToggle">🔗 Masters <span class="arrow">▼</span></a>
                    <ul id="mastersDropdown" class="dropdown">
                        <li><a href="#">Organization</a></li>
                        <li><a href="#">Organization Settings</a></li>
                        <li><a href="#">Users</a></li>
                        <li><a href="#">Designation</a></li>
                        <li><a href="#">User Management</a></li>
                        <li><a href="#">Area</a></li>
                        <li><a href="#">District</a></li>
                        <li><a href="#">State</a></li>
                        <li><a href="#">Hospital</a></li>
                        <li><a href="#">References</a></li>
                    </ul>
                </li>
                <li>
                    <a href="#" id="reportsToggle">📄 Reports <span class="arrow">▼</span></a>
                    <ul id="reportsDropdown" class="dropdown">
                        <li><a href="#">Detailed Blood Donation Report</a></li>
                    </ul>
                </li>
                <li><a href="#">📊 Dashboard</a></li>
            </ul>
        </aside>

        <div class="main-content">
            <div class="form-section">
                <div class="form-group">
                    <label for="designationName">Designation Name:<span>*</span></label>
                    <input type="text" id="designationName" name="designationName">
                    <label for="activeStatus" style="margin-left: 300px;">Active Status: <span>*</span></label>
                    <input type="radio" id="activeYes" name="activeStatus" value="Yes"> Yes
                    <input type="radio" id="activeNo" name="activeStatus" value="No"> No
                </div>
                <div class="button-group">
                    <button id="clearBtn">Clear</button>
                    <button id="saveBtn">Save</button>
                    <button id="updateBtn">Update</button>
                    <button id="deleteBtn">Delete</button>
                </div>
            </div>

            <div class="search-section">
                <input type="text" id="searchInput" placeholder="Search Designations">
            </div>

            <table class="designation-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Designation Name</th>
                        <th>Status</th>
                        
                    </tr>
                </thead>
                <tbody id="designationTableBody">
                    <!-- Table rows will be dynamically inserted here -->
                </tbody>
            </table>

            <div class="pagination" id="pagination">
                <button class="disabled">Previous</button>
                <button>1</button>
                <button>Next</button>
            </div>
        </div>
    </div>

    <footer class="footer">
        © 2024 Share & Care Palliative Care | All Rights Reserved
    </footer>

    <script>
        function toggleSidebar() {
            document.body.classList.toggle('sidebar-active');
        }

        document.getElementById('mastersToggle').addEventListener('click', function () {
            document.getElementById('mastersDropdown').classList.toggle('show');
        });

        document.getElementById('reportsToggle').addEventListener('click', function () {
            document.getElementById('reportsDropdown').classList.toggle('show');
        });
    </script>
</body>
</html>
<!-- Designation without sidebar------------------------------------------------------------------------------------------------------------------------ -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Designation Management</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 3px 20px;
            border-bottom: 2px solid #e0e0e0;
        }
        .header img {
            height: 50px;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
        }
        .user-info {
            text-align: right;
        }
        .user-info a {
            color: #007bff;
            text-decoration: none;
        }
        .navbar {
            background-color: red;
            color: white;
            padding: 10px 20px;
            /* text-align: left; */
            font-size: 18px;
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        .container {
            padding: 20px;
            margin-top: 20px;
            /* font-size: 15px; */
        }
        .form-section {
            margin-bottom: 20px;
        }
        .form-group {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .form-group span {
            color: red;
        }
        .form-group label {
            flex: 0 0 155px;
            font-weight: bold;
        }
        .form-group input[type="text"] {
            flex: 0 0 30%; /* Adjusted width to be half the original size */
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .form-group input[type="radio"] {
            margin-left: 15px;

            
        }
        .button-group {
            display: flex;
            justify-content: flex-end;
            gap: 20px;
            margin-top: 35px;
        }
        .button-group button {
            background-color: red;
            color: white;
            border: none;
            padding: 10px 55px;
            cursor: pointer;
            border-radius: 4px;
        }
        .button-group button:hover {
            background-color: darkred;
        }
        .search-section {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .search-section input {
            width: 150px;
            padding: 8px 30px 8px 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background: #fff url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/svgs/solid/search.svg') no-repeat right 8px center;
            background-size: 16px;
        }
        .designation-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .designation-table th, .designation-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        .designation-table th {
            background-color: #f2f2f2;
        }
        .pagination {
            display: flex;
            justify-content: flex-end;
        }
        .pagination button {
            padding: 5px 10px;
            margin-left: 5px;
            border: 1px solid #ddd;
            background-color: #f5f5f5;
            cursor: pointer;
        }
        .pagination .current-page {
            background-color: red;
            color: white;
        }
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #f9f9f9;
            font-size: 14px;
            color: #888;
            position: relative;
            bottom: 0;
            width: 100%;
            margin-top: 100px;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">
            <img src="https://storage.googleapis.com/a1aa/image/4JEeyOlRe2vfwoMPFJZxYX3hVQBx1YuhHb49DXnfS4z9JbuOB.jpg" alt="Organization Logo" width="50" height="50">

        </div>
        <div class="title">Share & Care Palliative Care</div>
        <div class="user-info">
            <div>Welcome! <a href="#">John Doe</a></div>
            <div>Last Logged in 31/01/2024 11:12 AM</div>
        </div>
    </header>
    
    <nav class="navbar">
        <i class="fas fa-bars"></i> &nbsp;&nbsp;Designation
    </nav>
    
    <div class="container">
        <div class="form-section">
            <div class="form-group">
                <label for="designationName">Designation Name:<span>*</span></label>
                &nbsp;&nbsp;<input type="text" id="designationName" name="designationName">
                <label for="activeStatus" style="margin-left: 300px;">Active Status: <span>*</span></label>
                <input type="radio" id="activeYes" name="activeStatus" value="Yes"> Yes
                <input type="radio" id="activeNo" name="activeStatus" value="No"> No
            </div>
            <div class="button-group">
                <button id="clearBtn">Clear</button>
                <button id="createBtn">Create</button>
                <button id="editBtn">Edit</button>
                <button id="saveBtn">Save</button>
            </div>
        </div>

        <div class="search-section">
            <input type="text" placeholder="Search">
        </div>
        
        <table class="designation-table">
            <thead>
                <tr>
                    <th>Designation Name</th>
                    <th>Active</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Technician</td>
                    <td>Yes</td>
                </tr>
                <!-- Add more rows as needed -->
            </tbody>
        </table>

        <div class="pagination">
            <button disabled>Previous</button>
            <button class="current-page">1</button>
            <button>Next</button>
        </div>
    </div>
    
    <div class="footer">
        &copy; 2024 Share & Care Palliative Care. All rights reserved.
    </div>

    <script>
        document.getElementById('clearBtn').addEventListener('click', function() {
            document.getElementById('designationName').value = '';
            const checkedRadio = document.querySelector('input[name="activeStatus"]:checked');
            if (checkedRadio) {
                checkedRadio.checked = false;
            }
        });

        document.getElementById('createBtn').addEventListener('click', function() {
            alert('Create button clicked');
        });

        document.getElementById('editBtn').addEventListener('click', function() {
            alert('Edit button clicked');
        });

        document.getElementById('saveBtn').addEventListener('click', function() {
            alert('Save button clicked');
        });
    </script>
</body>
</html>
