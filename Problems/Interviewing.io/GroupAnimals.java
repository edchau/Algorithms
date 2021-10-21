import java.util.*;

public class GroupAnimals {
    public static void main(String[] args) {
        // sort animals 
        Animal[] zoo = {new Cat("Alice"), new Dog("Bob"), new Bird("Mallory"),
                        new Dog("Hello"), new Dog("Tim"), new Cat("Sarah")};

        Arrays.sort(zoo, new Comparator<Animal>() {
            public int compare(Animal first, Animal second) {
                if (first.getClass().equals(second.getClass())) {
                    return 0;
                }
                return first.getClass().hashCode() - second.getClass().hashCode();
            }
        });
        System.out.println(Arrays.toString(zoo));

        // group in hashmap
        HashMap<Integer, List<Animal>> map = new HashMap<>();

        for (Animal a : zoo) {
            int key = a.getClass().hashCode();
            if (!map.containsKey(key)) {
                map.put(key, new LinkedList<>());
            }
            map.get(key).add(a);
        }

        for (int key : map.keySet()) {
            System.out.println(map.get(key).toString());
        }
    }

    public static class Animal {
        private String name;

        public Animal(String name) {
            this.name = name;
        }

        public void setName(String name){
            this.name = name;
        }

        public String toString() {
            return this.name;
        }
    }

    public static class Cat extends Animal {
        public Cat(String name) {
            super(name);
        }
    }

    public static class Dog extends Animal {
        public Dog(String name) {
            super(name);
        }
    }

    public static class Bird extends Animal {
        public Bird(String name) {
            super(name);
        }
    }
}
