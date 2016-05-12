import java.util.*;
import java.util.stream.Collectors;

public class ListComprehension {
    public static ArrayList<List<Object>> s_score = new ArrayList<List<Object>>();

    public static void create_list(){
        //                                    0               1        2          3       4
        //                                  DATE	      HOME/AWAY	  RESULT	 TEX    A&M
        List<Object> e1 = Arrays.asList("11/24/11",	       "Away",	  "W",	     27,	25);
        List<Object> e2 = Arrays.asList("11/25/10",	       "Home",	  "L",	     17,	24);
        List<Object> e3 = Arrays.asList("11/26/09",	       "Away",	  "W",	     49,	39);
        List<Object> e4 = Arrays.asList("11/27/08",	       "Home",	  "W",	     49,	9);
        List<Object> e5 = Arrays.asList("11/23/07",	       "Away",	  "L",	     30,	38);
        List<Object> e6 = Arrays.asList("11/24/06",	       "Home",	  "L",	     7,     12);
        List<Object> e7 = Arrays.asList("11/25/05",	       "Away",	  "W",	     40,	29);
        List<Object> e8 = Arrays.asList("11/26/04",	       "Home",	  "W",	     26,	13);
        List<Object> e9 = Arrays.asList("11/28/03",	       "Away",	  "W",	     46,	15);
        List<Object> e10 = Arrays.asList("11/29/02",	   "Home",	  "W",	     50,	20);
        List<Object> e11 = Arrays.asList("11/23/01",	   "Away",	  "W",	     21,	7);
        List<Object> e12 = Arrays.asList("11/24/00",	   "Home",	  "W",	     43,	17);
        List<Object> e13 = Arrays.asList("11/26/99",	   "Away",	  "L",	     16,	20);
        List<Object> e14 = Arrays.asList("11/27/98",	   "Home",	  "W",	     26,	24);
        List<Object> e15 = Arrays.asList("11/28/97",	   "Away",	  "L",	     16,	27);
        List<Object> e16 = Arrays.asList("11/29/96",	   "Home",	  "W",	     51,	15);
        List<Object> e17 = Arrays.asList("12/2/95",        "Away",	  "W",	     16,	6);
        List<Object> e18 = Arrays.asList("11/5/94",        "Home",	  "L",	     10,	34);
        List<Object> e19 = Arrays.asList("11/25/93",	   "Away",	  "L",	     9,     18);
        List<Object> e20 = Arrays.asList("11/26/92",	   "Home",	  "L",	     13,	34);
        List<Object> e21 = Arrays.asList("11/28/91",	   "Away",	  "L",	     14,	31);
        List<Object> e22 = Arrays.asList("12/1/90",        "Home",	  "W",	     28,	27);
        List<Object> e23 = Arrays.asList("12/2/89",        "Away",	  "L",	     10,	21);
        List<Object> e24 = Arrays.asList("11/24/88",	   "Home",	  "L",	     24,	28);
        List<Object> e25 = Arrays.asList("11/26/87",	   "Away",	  "L",	     13,	20);
        List<Object> e26 = Arrays.asList("11/27/86",	   "Home",	  "L",	     3,     16);
        List<Object> e27 = Arrays.asList("11/28/85",	   "Away",	  "L",	     10,	42);
        List<Object> e28 = Arrays.asList("12/1/84",        "Home",	  "L",	     12,	37);
        List<Object> e29 = Arrays.asList("11/26/83",	   "Away",	  "W",	     45,	13);
        List<Object> e30 = Arrays.asList("11/25/82",	   "Home",	  "W",	     53,	16);
        List<Object> e31 = Arrays.asList("11/26/81",	   "Away",	  "W",	     21,	13);
        List<Object> e32 = Arrays.asList("11/29/80",	   "Home",	  "L",	     14,	24);
        List<Object> e33 = Arrays.asList("12/1/79",        "Away",	  "L",	     7,     13);
        List<Object> e34 = Arrays.asList("12/2/78",        "Home",	  "W",	     22,	7);
        List<Object> e35 = Arrays.asList("11/26/77",	   "Away",	  "W",	     57,	28);
        List<Object> e36 = Arrays.asList("11/25/76",	   "Home",	  "L",	     3,     27);
        List<Object> e37 = Arrays.asList("11/28/75",	   "Away",	  "L",	     10,	20);
        List<Object> e38 = Arrays.asList("11/29/74",	   "Home",	  "W",	     32,	3);
        List<Object> e39 = Arrays.asList("11/22/73",	   "Away",	  "W",	     42,	13);
        List<Object> e40 = Arrays.asList("11/23/72",	   "Home",	  "W",	     38,	3);
        List<Object> e41 = Arrays.asList("11/25/71",	   "Away",	  "W",	     34,	14);
        List<Object> e42 = Arrays.asList("11/26/70",	   "Home",	  "W",	     52,	14);
        List<Object> e43 = Arrays.asList("11/27/69",	   "Away",	  "W",	     49,	12);
        List<Object> e44 = Arrays.asList("11/28/68",	   "Home",	  "W",	     35,	14);
        List<Object> e45 = Arrays.asList("11/23/67",	   "Away",	  "L",	     7,     10);
        List<Object> e46 = Arrays.asList("11/24/66",	   "Home",	  "W",	     22,	14);
        List<Object> e47 = Arrays.asList("11/25/65",	   "Away",	  "W",	     21,	17);
        List<Object> e48 = Arrays.asList("11/26/64",	   "Home",	  "W",	     26,	7);
        List<Object> e49 = Arrays.asList("11/28/63",	   "Away",	  "W",	     15,	13);
        List<Object> e50 = Arrays.asList("11/22/62",	   "Home",	  "W",	     13,	3);
        List<Object> e51 = Arrays.asList("11/23/61",	   "Away",	  "W",	     25,	0);
        List<Object> e52 = Arrays.asList("11/24/60",	   "Home",	  "W",	     21,	14);

        s_score.add(e1); s_score.add(e2); s_score.add(e3); s_score.add(e4); s_score.add(e5); s_score.add(e6); s_score.add(e7); s_score.add(e8); s_score.add(e9); s_score.add(e10);
        s_score.add(e11); s_score.add(e12); s_score.add(e13); s_score.add(e14); s_score.add(e15); s_score.add(e16); s_score.add(e17); s_score.add(e18); s_score.add(e19); s_score.add(e20);
        s_score.add(e21); s_score.add(e22); s_score.add(e23); s_score.add(e24); s_score.add(e25); s_score.add(e26); s_score.add(e27); s_score.add(e28); s_score.add(e29); s_score.add(e30);
        s_score.add(e31); s_score.add(e32); s_score.add(e33); s_score.add(e34); s_score.add(e35); s_score.add(e36); s_score.add(e37); s_score.add(e38); s_score.add(e39); s_score.add(e40);
        s_score.add(e41); s_score.add(e42); s_score.add(e43); s_score.add(e44); s_score.add(e45); s_score.add(e46); s_score.add(e47); s_score.add(e48); s_score.add(e49); s_score.add(e50);
        s_score.add(e51); s_score.add(e52);
    }

    // pipeline 1
    public static void stream1(){
        System.out.println("Select * from s_score");
        s_score.stream()
                .forEach(p -> System.out.println(p));
    }

    // pipeline 2
    public static void stream2(){
        System.out.println("Select * from s_score where result = W");
        s_score.stream()
                .filter(e -> e.get(2).equals("W"))
                .forEach(p -> System.out.println(p));
    }

    // pipeline 3
    public static void stream3(){
        System.out.println("Select * from s_score where TEX > 20 order by TEX");
        s_score.stream()
                .filter(e -> ((Integer) (e.get(3))) > 20)
                .sorted(Comparator.comparing(s -> (Integer) (s.get(3))))
                .forEach(p -> System.out.println(p));
    }

    // pipeline 4
    public static void stream4(){
        System.out.println("Select date, result from s_score");
        s_score.stream()
                .map(e -> {
                    String date = (String) e.get(0);
                    String result = (String) e.get(2);
                    return Arrays.asList(date, result);
                })
                .forEach(p -> System.out.println(p));
    }

}