from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date

class YouTubeFilterCreate(BaseModel):
    title_keywords: Optional[List[str]] = Field(None, description="List of keywords to search in video titles")
    description_keywords: Optional[List[str]] = Field(None, description="List of keywords to search in video descriptions")
    comments_keywords: Optional[List[str]] = Field(None, description="List of keywords to search in comments")
    exact_phrases: Optional[List[str]] = Field(None, description="List of exact phrases to search for in video titles")
    channel_name: Optional[List[str]] = Field(None, description="List of channel names to filter by")
    channel_subscriber_min: Optional[int] = Field(None, ge=0, description="Minimum subscriber count")
    channel_subscriber_max: Optional[int] = Field(None, ge=0, description="Maximum subscriber count")
    minimum_views: Optional[int] = Field(None, ge=0, description="Minimum view count")
    minimum_likes: Optional[int] = Field(None, ge=0, description="Minimum like count")
    minimum_comments: Optional[int] = Field(None, ge=0, description="Minimum comment count")
    minimum_comment_likes: Optional[int] = Field(None, ge=0, description="Minimum comment like count")
    upload_start_date: Optional[date] = Field(None, description="Start date for video uploads")
    upload_end_date: Optional[date] = Field(None, description="End date for video uploads")
    comment_start_date: Optional[date] = Field(None, description="Start date for comment extraction")
    comment_end_date: Optional[date] = Field(None, description="End date for comment extraction")
    video_type: Optional[str] = Field("standard", description="Type of video (standard, live, etc.)")
    duration_min: Optional[int] = Field(None, ge=0, description="Minimum video duration in seconds")
    duration_max: Optional[int] = Field(None, ge=0, description="Maximum video duration in seconds")

    # Custom Field Validators
    @field_validator("channel_subscriber_max")
    def validate_subscriber_range(cls, max_val, values):
        min_val = values.get("channel_subscriber_min")
        if min_val is not None and max_val is not None and min_val > max_val:
            raise ValueError("Minimum subscriber count cannot be greater than maximum")
        return max_val

    @field_validator("duration_max")
    def validate_duration_range(cls, max_val, values):
        min_val = values.get("duration_min")
        if min_val is not None and max_val is not None and min_val > max_val:
            raise ValueError("Minimum duration cannot be greater than maximum")
        return max_val

    @field_validator("upload_end_date")
    def validate_upload_dates(cls, end_date, values):
        start_date = values.get("upload_start_date")
        if start_date is not None and end_date is not None and start_date > end_date:
            raise ValueError("Upload start date cannot be after the end date")
        return end_date

    @field_validator("comment_end_date")
    def validate_comment_dates(cls, end_date, values):
        start_date = values.get("comment_start_date")
        if start_date is not None and end_date is not None and start_date > end_date:
            raise ValueError("Comment start date cannot be after the end date")
        return end_date
