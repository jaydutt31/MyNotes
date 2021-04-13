package main

import ("net/http"; "io"; "os")
...
out, err := os.Create("output.txt")
defer out.Close()
...
resp, err := http.Get("http://sourceforge.net/projects/espeak/files/espeak/espeak-1.48/setup_espeak-1.48.04.exe")
defer resp.Body.Close()
...
n, err := io.Copy(out, resp.Body)