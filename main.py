#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from caesar import encrypt
import webapp2
import cgi


form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            html {
                background-color: #00ee00;
            }
            form {
                background-color: #90ee90;
                padding: 50px;
                width: 640px;
                font: 16px sans-serif;
                margin: auto;
            }
            textarea {
                background-color: #eeeeee;
                margin: 10px 0;
                width: 640px;
                height: 120px;
                color: #009900;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="13">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(error)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

"""


class Caesar(webapp2.RequestHandler):


    def get(self):
        self.response.write(form % {"error": ""})


    def post(self):
        rot = self.request.get("rot")
        text = self.request.get("text")
        rot = int(rot)
        answer = encrypt(text, rot)
        answer_escaped = cgi.escape(answer)
        self.response.out.write(form % {"error": answer_escaped })


app = webapp2.WSGIApplication([
    ('/', Caesar)
], debug=True)
