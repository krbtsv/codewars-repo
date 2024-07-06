package src

func Invert(arr []int) []int {
	invArr := make([]int, len(arr))

	for i, num := range arr {
		invArr[i] = -num
	}
	return invArr
}
