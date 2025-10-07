# Cold Emailing Automation System

An AI-powered system for generating and sending personalized cold emails to potential professional contacts. This project combines OpenAI's GPT-4 for content generation with Gmail's API for automated email delivery.

## 🚀 Features

- **AI-Generated Emails**: Uses GPT-4 to create personalized cold emails based on recipient data
- **Gmail Integration**: Seamlessly creates drafts or sends emails through Gmail API
- **Batch Processing**: Handles large datasets of contacts efficiently
- **Customizable Templates**: Flexible prompt-based email generation framework
- **Progress Tracking**: Real-time progress bars for batch operations

## 📁 Project Structure

```
cold-emailing/
├── main.py                    # Email generation script
├── send_emails.py            # Gmail API integration for sending emails
├── test_send.py              # Testing utilities
├── cold_email_prompt_v2.txt  # Email generation framework/prompt
├── interns.csv               # Input data (contact information)
├── generated_emails.csv      # Output data (generated emails)
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🛠️ Setup

### Prerequisites

- Python 3.7+
- OpenAI API key
- Google Cloud Platform project with Gmail API enabled

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rohinsood/cold-emailing.git
   cd cold-emailing
   ```

2. **Install dependencies**
   ```bash
   pip install pandas tqdm openai google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

3. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

4. **Configure Gmail API**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Gmail API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the credentials file and save as `credentials.json`
   - Run the authentication flow (handled automatically on first run)

## 📊 Input Data Format

The system expects a CSV file (`interns.csv`) with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `FIRST NAME` | Recipient's first name | "John" |
| `LAST NAME` | Recipient's last name | "Doe" |
| `POSITION` | Job title/position | "Software Engineer Intern" |
| `COMPANY` | Company name | "Amazon" |
| `INDUSTRY` | Industry sector | "Information Technology & Services" |
| `KEYWORDS` | Relevant keywords/tags | "AI, machine learning, cloud computing" |
| `CITY` | Location city | "Seattle" |
| `STATE` | Location state | "Washington" |
| `COUNTRY` | Location country | "United States" |
| `EMAIL` | Email address | "john.doe@company.com" |
| `HYPERLINK ROLE` | LinkedIn profile URL | "https://linkedin.com/in/johndoe" |

## 🚀 Usage

### 1. Generate Emails

Run the email generation script to create personalized emails for all contacts:

```bash
python main.py
```

This will:
- Read contact data from `interns.csv`
- Generate personalized emails using GPT-4
- Save results to `generated_emails.csv`

### 2. Send Emails

After generating emails, use the Gmail integration to send them:

```bash
python send_emails.py
```

**⚠️ Important**: By default, the script creates **drafts** in Gmail rather than sending emails immediately. This allows you to review and modify emails before sending.

To send emails immediately, uncomment the send lines in `send_emails.py`:
```python
# Uncomment these lines to send immediately:
# service.users().messages().send(userId="me", body={"raw": raw}).execute()
# print(f"📨 Sent email to {to}")
```

## 📝 Email Generation Framework

The system uses a sophisticated prompt framework (`cold_email_prompt_v2.txt`) that generates emails with:

- **Personalized subject lines**
- **Student-to-student tone** (not corporate)
- **Specific connections** to recipient's role/company
- **Structured format** with introduction, connection, background, and closing
- **Professional sign-off** with contact information

### Example Generated Email

```
Subject: Quick chat about your experience at Amazon

Dear Frank,

My name is Rohin Sood, and I'm a freshman studying EECS at UC Berkeley. I came across your profile and was really interested in learning more about your experience as a Software Engineer Intern at Amazon.

I noticed you're working in cloud computing and AI services, which aligns perfectly with my current research at NASA Ames where I'm developing predictive modeling for spaceflight biology using machine learning techniques.

About me:
• EECS student at UC Berkeley (Class of 2029)
• Conducting AI/ML research at NASA Ames (predictive modeling for spaceflight biology)
• Built an AI tutoring assistant Chrome extension using NLP and Google Meet API
• Created a machine learning slap-bass transcription tool for automatic audio-to-notation

Would you be open to a brief informal chat about your experience at Amazon? I'm generally free from 3:30–6:30 PM PST and after 8:00 PM on most weekdays, but happy to adjust.

Best regards,
Rohin Sood
UC Berkeley EECS '29
LinkedIn: https://linkedin.com/in/rohin-sood
Portfolio: https://rohinsood.dev
```

## 🔧 Configuration

### Customizing Email Generation

Edit `cold_email_prompt_v2.txt` to modify:
- Email tone and style
- Personal background information
- Contact information
- Email structure and format

### Gmail API Scopes

The system requests these Gmail API permissions:
- `https://www.googleapis.com/auth/gmail.compose` - Create drafts
- `https://www.googleapis.com/auth/gmail.send` - Send emails

## 🔒 Security & Privacy

- **Credentials Protection**: All sensitive files (`credentials.json`, `token.json`) are excluded from version control
- **Environment Variables**: API keys are stored as environment variables
- **Draft Mode**: Default behavior creates drafts for review before sending

## 📈 Output

The system generates a CSV file (`generated_emails.csv`) with:
- Original contact data
- Generated subject lines
- Complete email bodies
- Error handling for failed generations

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Errors**
   - Verify your API key is set correctly
   - Check your OpenAI account credits/limits

2. **Gmail Authentication Issues**
   - Ensure `credentials.json` is in the project directory
   - Delete `token.json` to re-run authentication flow

3. **Permission Errors**
   - Verify Gmail API is enabled in Google Cloud Console
   - Check that your OAuth consent screen is configured

### Error Handling

The system includes comprehensive error handling:
- Failed email generations are logged with error details
- Authentication errors are caught and reported
- Progress is saved even if some emails fail

## 📄 License

This project is for educational and professional networking purposes. Please ensure compliance with:
- Recipients' privacy preferences
- Anti-spam regulations (CAN-SPAM Act, GDPR)
- Your organization's email policies

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the system.

## 📞 Contact

**Rohin Sood**
- LinkedIn: [https://linkedin.com/in/rohin-sood](https://linkedin.com/in/rohin-sood)
- Portfolio: [https://rohinsood.dev](https://rohinsood.dev)
- Email: Available upon request

---

*Built with ❤️ for efficient and authentic professional networking*
