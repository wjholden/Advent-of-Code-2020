import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Aoc2020Day15 {

    static int memoryGame(List<Integer> numbers, int limit, Map<Integer, Integer> dict) {
        IntStream.range(0, numbers.size()).forEach(i -> dict.put(numbers.get(i), i + 1) );
        int say = numbers.get(numbers.size() - 1);
        for (int i = numbers.size() ; i < limit ; i++) {
            int nextSay = i - dict.getOrDefault(say, i);
            dict.put(say, i);
            say = nextSay;
        }
        return say;
    }

    // Run with & 'C:\Program Files\jdk-14\bin\java.exe' Aoc2020Day15.java 30000000 2 1 10 11 0 6
    public static void main (String args[]) {
        // probably a smarter way to do this but it has been a while
        int limit = Integer.valueOf(args[0]);
        var numbers = Arrays.asList(args).stream().mapToInt(Integer::valueOf).boxed().collect(Collectors.toList());
        numbers.remove(0);

        // speed using a HashMap
        var start1 = Instant.now();
        int value1 = memoryGame(numbers, limit, new HashMap<Integer, Integer>());
        System.out.printf("Using HashMap: %s (value = %d)\n", Duration.between(start1, Instant.now()), value1);

        // speed using a TreeMap
        var start2 = Instant.now();
        int value2 = memoryGame(numbers, limit, new TreeMap<Integer, Integer>());
        System.out.printf("Using TreeMap: %s (value = %d)\n", Duration.between(start2, Instant.now()), value2);

        // My test gave 3.8 seconds for HashMap and 13.0 seconds for TreeMap.
    }
}