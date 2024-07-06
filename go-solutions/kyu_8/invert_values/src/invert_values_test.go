package src

import "testing"

func TestMax(t *testing.T) {
	numbers := []int{1, 2, 3, -1}
	expected := []int{-1, -2, -3, 1}

	result := Invert(numbers)

	if equalSlices(numbers, result) == false {
		t.Errorf("Incorrect result. Expect %d, got %d",
			expected, result)
	}
}

func equalSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}
