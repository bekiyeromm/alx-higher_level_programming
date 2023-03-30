#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
#!/bin/bash
curl -X PUT 0.0.0.0:5000/catch_me -sw "You got me!"
