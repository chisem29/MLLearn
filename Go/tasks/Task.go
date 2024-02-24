package main

import (
    "os"
    "strings"
    "time"
    "fmt"
)

type Queue struct {
    Q []int
}

func (this Queue) Empty() bool {
    return len(this.Q) == 0
}

func ExtractLog(inputFileName string, start, end time.Time) ([]string, error) {
    data, err := os.ReadFile(inputFileName)
    if err != nil {
        return nil, err
    }

    lines := strings.Split(string(data), "\n")

    filteredLines := make([]string, 0)

    for _, line := range lines {
        parts := strings.Split(line, " ")

        if len(parts) != 2 {
            continue
        }
        t, err := time.Parse("02.01.2006", parts[0])
        if err != nil {
            continue
        }
        if t.After(start.Add(-24 * 1)) && t.Before(end.Add(24*1)) {
            filteredLines = append(filteredLines, line)
        }
    }
    if len(filteredLines) == 0 {
        return nil, err
    }

    return filteredLines, nil
}

func main() {

    ss := []int{1, 2, 3}
    q := {ss}

    start, err := time.Parse("02.01.2006", "19.12.2022")
    if err != nil {
        panic(err)
    }
    end, err := time.Parse("02.01.2006", "20.12.2022")
    if err != nil {
        panic(err)
    }

    fmt.Println(ExtractLog("C:/Users/celin/MLLearn/Go/tasks/t.txt", start, end))
}