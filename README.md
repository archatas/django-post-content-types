# Django POST Content Types

This Django project demonstrates handling 9 different POST content types with separate views and proper CSRF token handling.

![Screenshot](screenshot.png)

## Quick Start

1. Run the development server:
```bash
python manage.py runserver
```

2. Open your browser to `http://127.0.0.1:8000/`

3. Click any button to test the corresponding POST format

## API Endpoints

- `POST /api/urlencoded/` - Handle URL-encoded form data
- `POST /api/multipart/` - Handle multipart form data
- `POST /api/json/` - Handle JSON
- `POST /api/ndjson/` - Handle NDJSON
- `POST /api/text/` - Handle plain text
- `POST /api/html/` - Handle HTML
- `POST /api/xml/` - Handle XML
- `POST /api/svg/` - Handle SVG
- `POST /api/binary/` - Handle binary data

All endpoints return JSON responses with the received data and metadata.

## CSRF Protection

All views use Django's built-in CSRF protection. The JavaScript code includes:
- `getCookie()` function to read the CSRF token from cookies
- `X-CSRFToken` header in all POST requests
- `@ensure_csrf_cookie` decorator on the index view to ensure the token is set

---

## Real-World Use Cases

### 1. application/x-www-form-urlencoded

**When to use:** Traditional HTML forms, simple key-value submissions

**Real-world examples:**
- **Login Forms:** Simple username/password authentication without file uploads
- **Contact Forms:** Name, email, subject, and message fields
- **Search Filters:** Submitting search queries with multiple filter parameters
- **Newsletter Subscriptions:** Email address and preference checkboxes
- **Settings Updates:** Toggling feature flags or updating simple configuration options

```javascript
// Example: Contact form submission
const params = new URLSearchParams();
params.append('name', 'John Doe');
params.append('email', 'john@example.com');
params.append('subject', 'Product Inquiry');
params.append('message', 'I would like more information...');

fetch('/api/urlencoded/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': getCSRFToken()
    },
    body: params
});
```

---

### 2. multipart/form-data

**When to use:** File uploads, forms with mixed text and binary data

**Real-world examples:**
- **Profile Picture Upload:** Users uploading avatar images along with profile information
- **Document Management Systems:** Uploading PDFs, Word docs, or spreadsheets with metadata (title, description, tags)
- **Job Application Forms:** Submitting resume, cover letter, and portfolio files with applicant details
- **Social Media Posts:** Creating posts with images/videos and caption text
- **Bulk Import Features:** Uploading CSV/Excel files for data import with configuration options

```javascript
// Example: Profile update with avatar
const formData = new FormData();
formData.append('username', 'john_doe');
formData.append('bio', 'Software developer');
formData.append('avatar', fileInput.files[0]);

fetch('/api/multipart/', {
    method: 'POST',
    headers: { 'X-CSRFToken': getCSRFToken() },
    body: formData
});
```

---

### 3. application/json

**When to use:** Modern REST APIs, single-page applications, mobile apps

**Real-world examples:**
- **User Registration/Login:** Sending user credentials and profile data to authentication endpoints
- **E-commerce Cart Operations:** Adding/updating items in shopping cart with product IDs, quantities, and options
- **Real-time Chat Messages:** Sending message content, timestamps, and metadata in messaging applications
- **API Integrations:** Webhooks from services like Stripe, GitHub, or Slack sending event data
- **Dashboard Analytics:** Submitting complex filter criteria, date ranges, and aggregation parameters

```javascript
// Example: User registration
fetch('/api/json/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
    },
    body: JSON.stringify({
        username: 'john_doe',
        email: 'john@example.com',
        preferences: { theme: 'dark', notifications: true }
    })
});
```

---

### 4. application/x-ndjson

**When to use:** Streaming data, bulk operations, log aggregation

**Real-world examples:**
- **Bulk Data Import:** Importing thousands of records efficiently (users, products, transactions)
- **Log Aggregation:** Sending application logs from multiple sources to centralized logging
- **Real-time Analytics:** Streaming event data for analytics processing
- **Machine Learning Datasets:** Uploading training data in streaming fashion
- **Database Migrations:** Transferring large datasets between systems line-by-line

```javascript
// Example: Bulk user import
const ndjsonData = `{"username":"john_doe","email":"john@example.com","role":"user"}
{"username":"jane_smith","email":"jane@example.com","role":"admin"}
{"username":"bob_jones","email":"bob@example.com","role":"user"}
{"username":"alice_wong","email":"alice@example.com","role":"moderator"}`;

fetch('/api/ndjson/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-ndjson',
        'X-CSRFToken': getCSRFToken()
    },
    body: ndjsonData
});
```

---

### 5. text/plain

**When to use:** Simple text content, logs, notes, raw text data

**Real-world examples:**
- **Note-Taking Apps:** Saving plain text notes or journal entries
- **Code Snippet Sharing:** Submitting raw code without formatting
- **Log File Uploads:** Sending application logs or error reports as plain text
- **Markdown Content:** Submitting markdown-formatted blog posts or documentation
- **Command Output:** Sending terminal/console output for debugging or support tickets

```javascript
// Example: Saving a note
const noteContent = `Meeting Notes - 2025-11-13

Discussed project timeline
Action items:
- Review design mockups
- Schedule follow-up meeting`;

fetch('/api/text/', {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'X-CSRFToken': getCSRFToken()
    },
    body: noteContent
});
```

---

### 6. text/html

**When to use:** Rich text editors, email templates, content management

**Real-world examples:**
- **WYSIWYG Editors:** Saving formatted content from rich text editors (TinyMCE, CKEditor)
- **Email Template Creation:** Designing and saving HTML email templates
- **Blog Post Publishing:** Submitting article content with HTML formatting
- **Newsletter Composition:** Creating HTML newsletters with styling and images
- **Documentation Systems:** Saving help articles or knowledge base entries with formatting

```javascript
// Example: Saving blog post content
const htmlContent = `<!DOCTYPE html>
<html>
<head><title>My Blog Post</title></head>
<body>
    <h1>Introduction to Django</h1>
    <p>Django is a <strong>powerful</strong> web framework...</p>
    <ul>
        <li>Fast development</li>
        <li>Secure by default</li>
        <li>Scalable</li>
    </ul>
</body>
</html>`;

fetch('/api/html/', {
    method: 'POST',
    headers: {
        'Content-Type': 'text/html',
        'X-CSRFToken': getCSRFToken()
    },
    body: htmlContent
});
```

---

### 7. application/xml

**When to use:** Legacy systems, SOAP APIs, enterprise integrations, RSS feeds

**Real-world examples:**
- **SOAP Web Services:** Integrating with enterprise systems (banking, ERP, CRM)
- **RSS/Atom Feed Submissions:** Publishing blog posts or podcast episodes
- **Healthcare Data Exchange:** HL7 or FHIR medical records transmission
- **E-commerce Integrations:** Product catalog updates to marketplaces (Amazon, eBay)
- **Configuration Management:** Uploading application settings or deployment configurations

```javascript
// Example: Product catalog update
const xmlData = `<?xml version="1.0" encoding="UTF-8"?>
<product>
    <sku>PROD-12345</sku>
    <name>Wireless Headphones</name>
    <price>99.99</price>
    <stock>150</stock>
    <category>Electronics</category>
</product>`;

fetch('/api/xml/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/xml',
        'X-CSRFToken': getCSRFToken()
    },
    body: xmlData
});
```

---

### 8. image/svg+xml

**When to use:** Vector graphics, icons, diagrams, charts

**Real-world examples:**
- **Icon Management Systems:** Uploading custom SVG icons for design systems
- **Data Visualization:** Saving dynamically generated charts and graphs
- **Logo Uploads:** Accepting vector logos for branding materials
- **Diagram Editors:** Saving flowcharts, mind maps, or architectural diagrams
- **Map Customization:** Uploading custom map overlays or geographic visualizations

```javascript
// Example: Saving a custom icon
const svgData = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/>
    <path d="M10 17l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z" fill="#4CAF50"/>
</svg>`;

fetch('/api/svg/', {
    method: 'POST',
    headers: {
        'Content-Type': 'image/svg+xml',
        'X-CSRFToken': getCSRFToken()
    },
    body: svgData
});
```

---

### 9. application/octet-stream

**When to use:** Binary files, encrypted data, raw byte streams

**Real-world examples:**
- **Encrypted File Storage:** Uploading encrypted backups or sensitive documents
- **Binary Protocol Data:** Sending proprietary binary format data (e.g., game saves, CAD files)
- **Image Processing:** Uploading raw image data for server-side processing
- **Audio/Video Chunks:** Streaming media data in chunks for real-time processing
- **Database Dumps:** Uploading binary database backup files

```javascript
// Example: Uploading encrypted data
const encryptedData = await encryptFile(originalFile);
const binaryData = new Uint8Array(encryptedData);

fetch('/api/binary/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/octet-stream',
        'X-CSRFToken': getCSRFToken()
    },
    body: binaryData
});
```

---

## Content Type Selection Guide

| Use Case | Recommended Format | Why? |
|----------|-------------------|------|
| Simple Form | `application/x-www-form-urlencoded` | Lightweight, browser default |
| File Upload | `multipart/form-data` | Handles binary files efficiently |
| REST API | `application/json` | Standard, easy to parse, widely supported |
| Bulk Operations | `application/x-ndjson` | Memory efficient streaming |
| Text Content | `text/plain` | Simple, no parsing needed |
| Rich Content | `text/html` | Preserves formatting |
| Legacy Systems | `application/xml` | Enterprise compatibility |
| Vector Graphics | `image/svg+xml` | Scalable, editable |
| Binary Data | `application/octet-stream` | Raw bytes, no encoding overhead |

---

## Testing the Examples

Each example in this project includes:
- ✅ Proper CSRF token handling
- ✅ Error handling for invalid data
- ✅ Content-type validation
- ✅ Response with received data for verification

Try modifying the examples in `templates/index.html` to test different scenarios!
