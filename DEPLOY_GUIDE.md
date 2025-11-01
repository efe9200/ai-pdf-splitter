# How to Make Your PDF Extractor Website Public

There are several ways to make your website accessible on the internet. Here are your options:

---

## Option 1: ngrok (Quickest - Takes 2 minutes)

**What it is:** A tool that creates a temporary public URL pointing to your local computer.

**Pros:**
- Free and instant
- No configuration needed
- Get a public URL in seconds
- Great for testing or temporary sharing

**Cons:**
- URL changes each time you restart
- Computer must stay on
- Free tier has bandwidth limits

**Steps:**

1. **Download ngrok:**
   - Go to https://ngrok.com/download
   - Create a free account
   - Download ngrok for Windows

2. **Install ngrok:**
   - Extract the downloaded file
   - Move `ngrok.exe` to your python_pdf folder

3. **Get your auth token:**
   - Login to https://dashboard.ngrok.com/
   - Copy your auth token
   - Run: `ngrok authtoken YOUR_TOKEN_HERE`

4. **Start your website first:**
   - Double-click `START_WEBSITE.bat`
   - Wait for it to say "Running on http://127.0.0.1:5000"

5. **Start ngrok:**
   - Open a new command prompt
   - Navigate to your python_pdf folder
   - Run: `ngrok http 5000`

6. **Share your URL:**
   - ngrok will show you a URL like: `https://abc123.ngrok.io`
   - Share this URL with anyone!
   - They can access your website from anywhere

---

## Option 2: PythonAnywhere (Best for Beginners - Free Tier Available)

**What it is:** A hosting platform specifically designed for Python applications.

**Pros:**
- Free tier available
- Easy to use
- Your URL stays the same
- No need to keep your computer on
- Good for learning

**Cons:**
- Free tier has limitations (100 seconds/day CPU time)
- URL is like: `yourusername.pythonanywhere.com`

**Steps:**

1. **Sign up:**
   - Go to https://www.pythonanywhere.com
   - Create a free account

2. **Upload your code:**
   - Use their web-based file browser
   - Upload `app.py` and the `templates` folder

3. **Install dependencies:**
   - Open a Bash console
   - Run: `pip install flask PyPDF2`

4. **Configure web app:**
   - Go to Web tab → Add a new web app
   - Choose Flask
   - Point to your `app.py` file

5. **Your site is live:**
   - Access at: `yourusername.pythonanywhere.com`

---

## Option 3: Render (Modern Cloud Hosting - Free Tier)

**What it is:** Modern cloud platform with generous free tier.

**Pros:**
- Free tier is generous
- Automatic deployments from GitHub
- Custom domain support
- Professional setup
- Always online

**Cons:**
- Requires GitHub account
- Slightly more technical
- Free apps "sleep" after 15 minutes of inactivity

**Steps:**

1. **Prepare your code:**
   - Create a `requirements.txt` file (see below)
   - Create a `render.yaml` file (see below)

2. **Push to GitHub:**
   - Create a GitHub repository
   - Upload your code

3. **Deploy on Render:**
   - Sign up at https://render.com
   - Click "New Web Service"
   - Connect your GitHub repository
   - Render will automatically deploy

---

## Option 4: Heroku (Industry Standard - Free Tier Ending)

**Note:** Heroku ended their free tier in 2022, now requires payment ($5-7/month minimum)

**What it is:** Popular cloud platform, very reliable.

**Pros:**
- Professional-grade
- Excellent documentation
- Easy scaling
- Custom domains

**Cons:**
- No longer free
- Requires credit card
- More complex setup

---

## Recommended Approach Based on Your Needs:

### For Quick Testing/Sharing (1-2 hours):
→ **Use ngrok** - Get a public URL in 2 minutes

### For Personal Use or Small Projects:
→ **Use PythonAnywhere** - Free, easy, always available

### For Professional/Business Use:
→ **Use Render or Heroku** - Reliable, scalable, professional

---

## Files Needed for Cloud Deployment

### requirements.txt
Create this file listing all Python packages:
```
Flask==3.1.2
PyPDF2==3.0.1
Werkzeug==3.1.3
```

### For Render - render.yaml
```yaml
services:
  - type: web
    name: pdf-extractor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
```

---

## Security Considerations

**IMPORTANT:** Before going public, update these in `app.py`:

1. **Change the secret key:**
   ```python
   app.secret_key = 'your-secret-key-here-change-in-production'
   ```
   Replace with a random string (at least 24 characters)

2. **Consider file size limits** - Currently set to 50MB max

3. **Add rate limiting** to prevent abuse

4. **Use HTTPS** (ngrok and cloud platforms provide this automatically)

---

## Need Help?

1. **ngrok tutorial:** https://ngrok.com/docs/getting-started
2. **PythonAnywhere tutorial:** https://help.pythonanywhere.com/pages/Flask/
3. **Render tutorial:** https://render.com/docs/deploy-flask

Let me know which option you'd like to use and I can help you set it up!
