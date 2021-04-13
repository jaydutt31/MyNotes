package main

import (
    "os/exec"
    "log"
)

func main() {
    s := "I love you"
    cmd := exec.Command("espeak", s)
    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}