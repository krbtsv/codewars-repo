import unittest

from katas.kyu_5.factorial_decomposition import decomp


class DecompTestCase(unittest.TestCase):
    def test_decomp(self):
        self.assertEqual(decomp(5), "2^3 * 3 * 5")
        self.assertEqual(decomp(14), "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13")
        self.assertEqual(decomp(17), "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17")
        self.assertEqual(decomp(22), "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19")
        self.assertEqual(decomp(25), "2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23")
        self.assertEqual(decomp(79),
                         "2^74 * 3^36 * 5^18 * 7^12 * 11^7 * 13^6 * 17^4 * 19^4 * 23^3 * 29^2 * 31^2 * 37^2 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73 * 79")
        self.assertEqual(decomp(98),
                         "2^95 * 3^46 * 5^22 * 7^16 * 11^8 * 13^7 * 17^5 * 19^5 * 23^4 * 29^3 * 31^3 * 37^2 * 41^2 * 43^2 * 47^2 * 53 * 59 * 61 * 67 * 71 * 73 * 79 * 83 * 89 * 97")
        self.assertEqual(decomp(3988),
                         "2^3981 * 3^1990 * 5^994 * 7^662 * 11^396 * 13^330 * 17^247 * 19^220 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967")
        self.assertEqual(decomp(3989),
                         "2^3981 * 3^1990 * 5^994 * 7^662 * 11^396 * 13^330 * 17^247 * 19^220 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967 * 3989")
        self.assertEqual(decomp(3990),
                         "2^3982 * 3^1991 * 5^995 * 7^663 * 11^396 * 13^330 * 17^247 * 19^221 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967 * 3989")
