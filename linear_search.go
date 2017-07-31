package main

import ("fmt"
        "bufio"
        "os"
        "strconv"
        "strings"
        )

func cleanString(stream string, seperator string) []int{
  // Trims the stream and then splits
  trimmed_stream := strings.TrimSpace(stream)
  split_arr := strings.Split(trimmed_stream, seperator)
  // convert strings to integers and store them in a slice
  clean_arr := make([]int, len(split_arr))
  for index,val := range split_arr{
    clean_arr[index], _ = strconv.Atoi(val)
  }
  return clean_arr
}


func main() {
	inputreader := bufio.NewReader(os.Stdin)
	ln1, _ := inputreader.ReadString('\n')
	ln2, _ := inputreader.ReadString('\n')
	meta_data := cleanString(ln1," ")
	array := cleanString(ln2," ")
	found := -1
	for i,v := range array{
	    if v==meta_data[1]{
	        found = i
	    }
	}
	fmt.Println(found)
}
