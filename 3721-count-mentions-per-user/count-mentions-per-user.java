class Solution {
    //Aryan
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        int[] mentions = new int[numberOfUsers];
        Map<Integer, Integer> offlineMap = new HashMap<>();
        Set<Integer> onlineUsers = new HashSet<>();
        for (int i = 0; i < numberOfUsers; i++) {
            onlineUsers.add(i);
        }

        events.sort((a, b) -> {
            int timeA = Integer.parseInt(a.get(1));
            int timeB = Integer.parseInt(b.get(1));
            if (timeA != timeB) {
                return timeA - timeB;
            }
            return a.get(0).equals("OFFLINE") ? -1 : 1;
        });

        int currTime = 0;

        for (List<String> event : events) {
            String eventType = event.get(0);
            int timestamp = Integer.parseInt(event.get(1));
            String data = event.get(2);

            if (timestamp > currTime) {
                currTime = timestamp;

                List<Integer> toRemove = new ArrayList<>();

                for (Map.Entry<Integer, Integer> entry : offlineMap.entrySet()) {
                    int userId = entry.getKey();
                    int offlineTime = entry.getValue();

                    if (currTime - offlineTime >= 60) {
                        toRemove.add(userId);
                        onlineUsers.add(userId);
                    }
                }

                for (int userId : toRemove) {
                    offlineMap.remove(userId);
                }
            }

            if (eventType.equals("OFFLINE")) {
                int userId = Integer.parseInt(data);
                onlineUsers.remove(userId);
                offlineMap.put(userId, currTime);
            } else if (eventType.equals("MESSAGE")) {
                if (data.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (data.equals("HERE")) {
                    List<Integer> toRemove = new ArrayList<>();
                    for (Map.Entry<Integer, Integer> entry : offlineMap.entrySet()) {
                        int userId = entry.getKey();
                        int offlineTime = entry.getValue();

                        if (currTime - offlineTime >= 60) {
                            toRemove.add(userId);
                            onlineUsers.add(userId);
                        }
                    }

                    for (int userId : toRemove) {
                        offlineMap.remove(userId);
                    }

                    for (int userId : onlineUsers) {
                        mentions[userId]++;
                    }
                } else {
                    String[] tokens = data.split(" ");
                    for (String token : tokens) {
                        if (token.startsWith("id")) {
                            int userId = Integer.parseInt(token.substring(2));
                            mentions[userId]++;
                        }
                    }
                }
            }
        }

        return mentions;
    }
}