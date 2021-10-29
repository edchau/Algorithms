import java.util.*;

public class GroupNames {

    final static String DICTIONARY = "alex,alexander\nnick,nicholas,nate\nsally,sal";
    public static void main(String[] args) {
        Person[] contacts = new Person[]
        {new Person("sarah", "kim"), new Person("sally", "tran"), 
        new Person("lucas", "nguyen"), new Person("nick", "kim"),
        new Person("sal", "tran"), new Person("kevin", "chau"),
        new Person("nate", "kim"), new Person("lucas", "nguyen")};

        HashMap<String, List<Person>> map = groupPeople(contacts);
        for (String entry : map.keySet()) {
            String value = map.get(entry).toString();
            System.out.println(entry + "" + value + " ");
        }
    }

    public static HashMap<String, List<Person>> groupPeople(Person[] contacts) {

        HashMap<String, List<Person>> groups = new HashMap<>();

        // MAP DICTIONARY
        // nick -> nicholas -> nate
        String[] dict = DICTIONARY.split("\\n"); 
        
        HashMap<String, HashSet<String>> aliases = new HashMap<>();

        for (String names : dict) {
            HashSet<String> same = new HashSet<>();
            for (String alias : names.split(",")) {
                same.add(alias);
                aliases.put(alias, same);
            }
        }

        // for (String entry : aliases.keySet()) {
        //     String value = aliases.get(entry).toString();
        //     System.out.print(entry + "" + value + " ");
        // }

        for (Person p : contacts) {
            String first = p.firstName;
            String last = p.lastName;
            String full = first + " " + last;
            if (groups.containsKey(full)) {
                groups.get(full).add(p);
            } else {
                boolean found = false;
                for (String alias : aliases.getOrDefault(first, new HashSet<>())) {
                    String alt = alias + " " + last;
                    if (groups.containsKey(alt)) {
                        groups.get(alt).add(p);
                        found = true;
                        break;
                    }
                }
                if (!found)
                    groups.put(full, new ArrayList<>());
            }
        }

        return groups;
    }

    public static class Person {
        private String firstName;
        private String lastName;

        public Person(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public String toString() {
            return this.firstName + " " + this.lastName;
        }
    }
}
