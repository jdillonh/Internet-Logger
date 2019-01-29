# Internet-Logger
A script for MacOS and Linux to monitor when your internet is up and when it is not.

Output is logged in `log.txt`. It keeps track of when connection is lost, and when it is restored.


It prints nothing, but instead displays notifications on MacOS using AppleScript ("osascript"). Linux users can fill in the `notify(m)` function at line 15 to work with their DE.

