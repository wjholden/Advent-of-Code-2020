function memory_game($a, $limit) {
    $i = 0
    $say = 0
    $said = @{}

    while ($i -lt $limit) {
        if ($i -lt $a.Length) {
            $say = $a[$i]
            $said[$a[$i]] = $i
        } else {
            if ($said.ContainsKey($say)) {
                $diff = $i - $said[$say] - 1
                $said[$say] = $i - 1
                $say = $diff
            } else {
                $said[$say] = $i - 1
                $say = 0
            }
        }
        $i++;
        #"$($i)`t$($say)"
    }
    return $say
}

memory_game @(2,1,10,11,0,6) 30000000