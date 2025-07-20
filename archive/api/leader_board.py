

async def leaderboard_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Handle /leaderboard command"""
    try:
        leaderboard = await rq_analytics.get_leaderboard(limit=10)

        if leaderboard:
            leaderboard_text = "🏆 Top Performers\n\n"
            for i, user in enumerate(leaderboard, 1):
                score = user.average_overall_score or 0
                leaderboard_text += f"{i}. {user.first_name} - {score:.1f}/9.0 ({user.total_responses} responses)\n"
        else:
            leaderboard_text = "No users have practiced yet. Be the first! 🚀"

        await update.message.reply_text(leaderboard_text)

    except Exception as e:
        logger.error(f"Error getting leaderboard: {e}")
        await update.message.reply_text(
            "Sorry, there was an error getting the leaderboard."
        )
