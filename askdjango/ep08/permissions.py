from rest_framework import permissions


class IsAuthorUpdateOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회/포스팅등록을 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # superuser에게는 삭제 권한만 부여하고
    # 작성자에게는 수정 권한만 부여
    def has_object_permission(self, request, view, obj):
        # 조회 요청(GET, HEAD, OPTIONS)의 경우, 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # DELETE 요청의 경우, superuser에게만 허용
        if request.method == 'DELETE':
            return request.user.is_superuser    # request.user.is_staff

        # PUT 요청의 경우, 작성자일 경우에만 요청 허용
        return obj.author == request.user