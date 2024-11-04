import random

# Full list of 100 therapy questions
questions = [
    # Initial Session and Background Questions
    "What has been going well for you lately?",
    "What do you think brought you to this point in your life?",
    "Have you had any major life changes recently?",
    "What do you hope to learn about yourself through therapy?",
    # Relationship and Support Questions
    "Do you feel supported by the people closest to you?",
    "Are there people in your life you find it hard to communicate with?",
    "Who do you feel most comfortable opening up to?",
    "How would you describe your current relationships with friends and family?",
    # Emotional and Mental Health Questions
    "How often do you feel overwhelmed or stressed?",
    "What are some things you do that bring you joy or help you relax?",
    "How would you rate your overall mood on a scale from 1 to 10?",
    "Do you have trouble sleeping? How does it affect your day?",
    # Coping and Self-Reflection Questions
    "What are some of the biggest challenges you're currently facing?",
    "What helps you get through difficult times?",
    "Can you think of a time when you handled a challenge well?",
    "What does self-care look like for you right now?",
    # Goal-Oriented Questions
    "What are some personal goals or changes you’d like to make?",
    "What would a 'good day' look like for you?",
    "How would you like to feel or think differently?",
    "What do you see as your biggest strength?",
    # Cognitive Exploration Questions (Inspired by CBT)
    "What beliefs do you hold that might not be helping you?",
    "How often do you find yourself worrying about things out of your control?",
    "Is there a more helpful way to view this situation?",
    "If a friend were in your shoes, what advice would you give them?",
    # Present-Moment Questions (Mindfulness)
    "What sensations do you feel in your body right now?",
    "Is there anything happening right now that’s causing you discomfort or peace?",
    "If you could describe how you feel in one word, what would it be?",
    "How aware are you of your breathing at this moment?",
    # Personal Values and Identity Questions
    "What are some things that truly matter to you?",
    "How would you describe yourself in three words?",
    "What do you feel proud of in your life?",
    "Who do you want to become, and what steps can you take to get there?",
    # Self-Awareness and Reflection
    "What makes you feel most alive?",
    "How do you usually respond to stress?",
    "What are some things you feel grateful for?",
    "What would you like to understand more about yourself?",
    # Life and Future Goals
    "If you could change one thing in your life, what would it be?",
    "What’s something you’d like to achieve this year?",
    "Where do you see yourself in the next five years?",
    "What’s a dream you’ve had since childhood?",
    # Problem Solving and Challenges
    "What is a problem you recently solved on your own?",
    "Who do you turn to when you face a challenge?",
    "How do you feel after overcoming a difficult situation?",
    "What’s the hardest thing you’ve ever had to do?",
    # Personal Strengths and Motivation
    "What’s something you’re proud of accomplishing?",
    "Who inspires you, and why?",
    "What motivates you to get through tough times?",
    "What are some qualities you admire in others?",
    # Emotional Check-Ins
    "When was the last time you felt truly at peace?",
    "Are there any emotions you’ve been holding back?",
    "What would make you feel happier right now?",
    "How often do you feel understood by those around you?",
    # Self-Exploration and Values
    "What values are most important to you in life?",
    "If you could go back in time, what advice would you give your younger self?",
    "What qualities in people do you admire most?",
    "When do you feel most at peace with yourself?",
    "How do you want to be remembered by others?",
    "What do you consider your most defining moments?",
    "Who are the people who have influenced you the most, and why?",
    "What does happiness mean to you?",
    "How do you deal with changes in your life?",
    "What life experiences have shaped your core beliefs?",
    # Goals and Aspirations
    "What are some goals you haven’t achieved yet but would like to?",
    "If money weren’t a concern, how would you spend your life?",
    "What are some ways you can make a difference in the world?",
    "What new skills or hobbies would you like to learn?",
    "What legacy would you like to leave behind?",
    "How would you describe your dream lifestyle?",
    "If you could write a book, what would it be about?",
    "What are some barriers you face when pursuing your goals?",
    "How do you measure success in your life?",
    "What is a goal you feel particularly proud of achieving?",
    # Relationships and Boundaries
    "How do you manage conflicts in relationships?",
    "How do you communicate your needs to others?",
    "Do you feel comfortable saying 'no' when you need to?",
    "What’s a relationship you’re grateful for, and why?",
    "How do you handle criticism or negative feedback?",
    "What are some personal boundaries you have set for yourself?",
    "What do you need from relationships to feel fulfilled?",
    "How do you feel when others rely on you?",
    "What’s a challenging relationship you've overcome?",
    "Who has been there for you during tough times?",
    # Coping Strategies and Resilience
    "What are some things that make you feel resilient?",
    "How do you find strength when you’re feeling down?",
    "What’s a coping mechanism you’ve found helpful?",
    "What role does humor play in your life?",
    "How do you usually react to disappointments?",
    "What activities help you clear your mind?",
    "What’s something you’ve learned from a difficult experience?",
    "What do you turn to when you need comfort?",
    "How do you manage expectations for yourself?",
    "What’s a comforting memory you turn to when stressed?",
    # Self-Awareness and Mindfulness
    "When was the last time you felt truly present?",
    "What daily habits do you have that help you stay grounded?",
    "How often do you take time to reflect on your day?",
    "Do you find it easy or difficult to sit in silence?",
    "What are some things you notice about yourself in stressful situations?",
    "What does your inner voice sound like?",
    "How do you stay in touch with your feelings?",
    "How aware are you of your physical sensations during the day?",
    "What do you appreciate about the present moment?",
    "What’s one thing you can do to bring more mindfulness into your life?",
    # Life Reflection and Personal Growth
    "How have your goals changed over time?",
    "What’s a lesson you learned recently that surprised you?",
    "What are some beliefs you held that you now see differently?",
    "How do you think you’ve grown over the past year?",
    "What do you feel you need more of in your life right now?",
    "How has your perspective on life changed over the years?",
]

print("Welcome to your therapy session! Type anything to begin:")
while True:
    user_input = input("Your input: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Thank you for using the therapy app. Take care!")
        break
    question = random.choice(questions)
    print(f"Therapist: {question}")
