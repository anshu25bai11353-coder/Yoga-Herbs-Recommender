print("🧘 Smart Yoga & Jadi-Buti Health Advisor 🪴")
print("⚠️ Educational purpose only\n")

# -------- USER INTAKE --------
problem = input("1️⃣ Apni main problem likhiye: ").lower()
symptoms = input("2️⃣ Symptoms likhiye (comma separated): ").lower()
duration = input("3️⃣ Kitne time se problem hai? (days/weeks/months): ").lower()
age = int(input("4️⃣ Aapki age kya hai?: "))
lifestyle = input("5️⃣ Lifestyle (active/sedentary): ").lower()
sleep = input("6️⃣ Sleep quality (good/average/poor): ").lower()
existing = input("7️⃣ Koi existing disease hai? (yes/no): ").lower()

user_text = problem + " " + symptoms

# -------- KNOWLEDGE BASE --------
database = {
    "mental": {
        "keywords": ["stress", "anxiety", "tension", "sleep", "insomnia"],
        "yoga": [
            {"name": "Anulom Vilom", "duration": "10 minutes"},
            {"name": "Meditation", "duration": "15 minutes"}
        ],
        "herb": "Ashwagandha",
        "reason": "Stress hormone (cortisol) ko kam karta hai aur mind ko calm karta hai"
    },

    "digestive": {
        "keywords": ["gas", "acidity", "indigestion", "constipation", "nausea" ,"loose motion", ],
        "yoga": [
            {"name": "Vajrasana", "duration": "10–15 minutes"},
            {"name": "Pawanmuktasana", "reps": "15 repetitions"}
        ],
        "herb": "Amla",
        "reason": "Digestive enzymes ko stimulate karta hai aur acidity balance karta hai"
    },

    "pain": {
        "keywords": ["pain", "ache", "headache", "back", "joint", "body pain", "sir me dard", "migraine","eyer", ],
        "yoga": [
            {"name": "Balasana", "duration": "5 minutes"},
            {"name": "Bhujangasana", "reps": "10 repetitions"}
        ],
        "herb": "Nirgundi",
        "reason": "Anti-inflammatory properties pain aur stiffness kam karti hain"
    },

    "respiratory": {
        "keywords": ["cold", "cough", "breath", "asthma", "flu", "khasi", "zukhaam","sardi"],
        "yoga": [
            {"name": "Kapalbhati", "reps": "20–30 strokes"},
            {"name": "Pranayama", "duration": "10 minutes"}
        ],
        "herb": "Tulsi + Ginger",
        "reason": "Antibacterial aur immunity-boosting effect hota hai"
    }
}

# -------- ANALYSIS --------
print("\n🔍 Health Analysis Result:\n")
matched = False

for category, data in database.items():
    for word in data["keywords"]:
        if word in user_text:
            matched = True
            print(f"🩺 Problem Category: {category.capitalize()}")

            print("\n🧘 Recommended Yoga:")
            for y in data["yoga"]:
                if "duration" in y:
                    print(f"  - {y['name']} : {y['duration']}")
                else:
                    print(f"  - {y['name']} : {y['reps']}")

            print(f"\n🌿 Jadi-Buti: {data['herb']}")
            print(f"❓ Reason: {data['reason']}")

            # -------- PERSONALIZED NOTES --------
            if age > 50:
                print("👴 Age factor → slow & supported yoga follow karein")
            if sleep == "poor":
                print("😴 Sleep issue → raat ko meditation zaroor add karein")
            if lifestyle == "sedentary":
                print("🚶 Lifestyle note → daily light movement add karein")
            if existing == "yes":
                print("👨‍⚕️ Existing condition → doctor se consult zaruri")

            print("\n---------------------------------\n")
            break

if not matched:
    print("⚠️ Problem clearly classify nahi ho paayi.")
    print("🧘 Safe Yoga: Gentle Pranayama (10 min), Meditation (10 min)")
    print("🌿 Safe Jadi-Buti: Tulsi, Giloy")
    print("❓ Reason: Ye immunity aur mental balance ko support karte hain")
    print("👨‍⚕️ Advice: Medical expert se consult karein")
print("   ")
print("   ")
print("   ")
print(" fix bill : free ")