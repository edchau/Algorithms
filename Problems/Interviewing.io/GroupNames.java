import java.util.*;

public class GroupNames {

    final static String DICTIONARY = "Alex,Alexander\nNick,Nicholas,Nate\nSally,Sal";
    public static void main(String[] args) {
        
    }

    public static HashMap<String, List<Person>> groupPeople(Person[] contacts) {
        return null;
    }

    public static class Person {
        private String name;

        public Person(String name) {
            this.name = name;
        }

        public void setName(String name){
            this.name = name;
        }

        public String toString() {
            return this.name;
        }
    }
}
