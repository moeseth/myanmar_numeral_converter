<?php

    function english_to_myanmar_digits($english_digits) {
        $myanmar_digits = $english_digits;

        $myanmar_digits = str_replace("0", "\xE1\x81\x80", $english_digits);
        $myanmar_digits = str_replace("1", "\xE1\x81\x81", $myanmar_digits);
        $myanmar_digits = str_replace("2", "\xE1\x81\x82", $myanmar_digits);
        $myanmar_digits = str_replace("3", "\xE1\x81\x83", $myanmar_digits);
        $myanmar_digits = str_replace("4", "\xE1\x81\x84", $myanmar_digits);
        $myanmar_digits = str_replace("5", "\xE1\x81\x85", $myanmar_digits);
        $myanmar_digits = str_replace("6", "\xE1\x81\x86", $myanmar_digits);
        $myanmar_digits = str_replace("7", "\xE1\x81\x87", $myanmar_digits);
        $myanmar_digits = str_replace("8", "\xE1\x81\x88", $myanmar_digits);
        $myanmar_digits = str_replace("9", "\xE1\x81\x89", $myanmar_digits);

        return $myanmar_digits;
    }

    function english_digits_to_myanmar_words($english_digits) {
        $utf_8_for_creaky_tone = "\xE1\x80\xB7"; // ့
        $myanmar_counting_number_array = array("သုည", "တစ်", "နှစ်", "သုံး", "လေး", "ငါး", "ခြောက်", "ခုနစ်", "ရှစ်", "ကိုး");
        $myanmar_counting_number_suffixes_array = array("ဆယ်", "ရာ", "ထောင်", "သောင်း", "သိန်း");

        $english_int_digits = intval($english_digits);

        $count = 5;

        $myanmar_words = "";

        while ($english_int_digits >= 10) {
            $powered_10 = pow(10, $count);

            if ($english_int_digits >= $powered_10) {
                $prefix_int = intval($english_int_digits/$powered_10);

                // minus found value from original value
                $english_int_digits = $english_int_digits - intval($powered_10 * $prefix_int);

                $suffix = "";
                if ($english_int_digits > 0 && $count > 0 && $count < 4) {
                    $suffix = $utf_8_for_creaky_tone;
                }

                if ($prefix_int > 9) {
                    $myanmar_words = $myanmar_words . english_digits_to_myanmar_words($prefix_int);
                } else {
                    $myanmar_words = $myanmar_words . $myanmar_counting_number_array[$prefix_int];
                }

                $myanmar_words = $myanmar_words . $myanmar_counting_number_suffixes_array[$count - 1] . $suffix;
            }

            $count = $count - 1;
        }

        if ($english_int_digits > 0) {
            $myanmar_words = $myanmar_words . $myanmar_counting_number_array[$english_int_digits];
        }

        return $myanmar_words;
    }

?>
