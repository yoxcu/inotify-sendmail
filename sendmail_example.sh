swaks --from john.smith@mydomain.com \
--h-From: '"John Smith" <john.smith@mydomain.com>' \
--h-Subject: 'Subject of message' \
--auth LOGIN --auth-user mylogin --auth-pass mypass \
--to someone@otherdomain.com \
--server smtp.example.com --port 25 -tls \
--add-header 'Content-Type: text/plain; charset="utf-8"' \
--body "$1"
